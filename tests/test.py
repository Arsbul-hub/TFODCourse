import os

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image


# for i, image in enumerate(os.listdir("./originals")):
#     img = Image.open(f"./originals/{image}")
#     if "sec" in image:
#         img.save(f"./enumerated/{i}_sec.jpg")
#     else:
#         img.save(f"./enumerated/{i}.jpg")

def modify_white(img):
    l = 0
    pil_img = Image.fromarray(img)
    w, h = pil_img.size
    pixmap = pil_img.load()
    pixels = []
    for y in range(w):
        for x in range(h):
            l += pixmap[y, x]
    sr = l // (w * h)
    for y in range(w):
        for x in range(h):
            if pixmap[y, x] < sr:
                pixels.append((x, y))
    return pil_img, pixels


def modify_black(img):
    l = 0
    pil_img = Image.fromarray(img)
    w, h = pil_img.size
    pixmap = pil_img.load()
    pixels = []
    for y in range(w):
        for x in range(h):
            l += pixmap[y, x]
    sr = l // (w * h)
    for y in range(w):
        for x in range(h):
            if pixmap[y, x] > sr:
                pixels.append((x, y))
    return pil_img, pixels


img1 = cv.imread(f"./enumerated/0.jpg", cv.IMREAD_GRAYSCALE)
img2 = cv.imread(f"./enumerated/1.jpg", cv.IMREAD_GRAYSCALE)

print("Loaded")
# print(image)

pil_img1, pixels1 = modify_white(img1)
print("Checked 1")
pil_img2, pixels2 = modify_black(img2)

print("Checked 2")
pix1 = pil_img1.load()
pix2 = pil_img2.load()
w1, h1 = pil_img1.size
w2, h2 = pil_img2.size
new = Image.new("RGBA", pil_img2.size)
new.paste(pil_img2)
# new2 = Image.new("RGBA", pil_img1.size)
# new2.paste(pil_img2)
# new2.putalpha(100)
# black_image = Image.new("RGBA", pil_img2.size)
# black_image.paste(pil_img2)
# pixels_map = black_image.load()
#
# for y in range(black_image.height):
#     for x in range(black_image.width):
#         r, g, b, a = pixels_map[x, y]
#
#         black_image.putpixel((x, y), (r, g, b, 10))
# new.paste(new2)
# new2.show()
print(f"Viewing {len(pixels1) * len(pixels2)} elements")
out = list(set(pixels1) & set(pixels2))
print(len(out))
print(f"Coloring {len(out)} pixels")
for x, y in out:
    try:
        new.putpixel((y, x), (255, 0, 0))
    except:
        print(y, x)
print("Done")
new.show()
new.save("out.png")

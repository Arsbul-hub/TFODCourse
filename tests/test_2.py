from PIL import Image

img = Image.open("./enumerated/0.jpg")
img = img.convert("L")
pixels = img.load()
img2 = Image.new("RGB", img.size)
img2.paste(img)

for y in range(img.height):
    old_pixels = []
    for x in range(img.width):
        current_pixel = img.getpixel((x, y))
        sr = 0
        for o in old_pixels:
            sr += o - min(old_pixels)
        sr = sr / 5
        if sr > 10:
            img2.putpixel((x, y), (255, 0, 0))
        if len(old_pixels) < 50:

            old_pixels.append(current_pixel)
        else:
            old_pixels.clear()
img2.show()
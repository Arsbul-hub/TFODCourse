import os

from os.path import isfile, join
onlyfiles = [f for f in os.listdir("./test") if isfile(join("./test", f))]
for i in onlyfiles:
    name, f = i.split(".")
    os.rename(f"./test/{i}", f'./dd/{int(name) - 3}.png')
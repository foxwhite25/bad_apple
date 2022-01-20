import concurrent.futures
import json
import random
from multiprocessing import Pool
from time import sleep

from PIL import Image

record = json.load(open("./temp.json"))


def intensity(image, pixels):
    left, up = pixels
    right, down = left + 32, up + 24
    count, total = 0, 0
    for x in range(left, right):
        for y in range(up, down):
            count += 1
            total += image.getpixel((x, y))[0]
    return int(total / count)


def process(frame: int):
    if frame % 100 == 0:
        print('Frame: ', frame)
    im = Image.open(f"./frame/frame{frame}.jpg")
    for x in range(0, 30):
        for y in range(0, 30):
            a = intensity(im, (x * 32, y * 24))
            if a in [0, 255]:
                continue
            b = record[str(a)]
            b = random.choice(b)
            im2 = Image.open(f"./frame/frame{b}.jpg")
            im2 = im2.resize((32, 24))
            im.paste(im2, (x * 32, y * 24))
    im.save(f"./result/frame{frame}.jpg")


if __name__ == '__main__':
    with Pool(8) as p:
        p.map(process, list(range(1000, 6572)))

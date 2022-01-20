import concurrent.futures
import json

from PIL import Image

record = {}


def intensity(frame):
    if frame % 100 == 0:
        print('Frame: ', frame)
    image = Image.open(f"./frame/frame{frame}.jpg")
    im1 = list(Image.Image.getdata(image))
    width, height = image.size
    count = width * height
    total = 0
    for pixel in im1:
        total += pixel[0]
    x = int(total / count)
    if x in record:
        record[x].append(frame)
    else:
        record[x] = [frame]


if __name__ == '__main__':
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        future_to_url = {executor.submit(intensity, n): n for n in range(6572)}
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            data = future.result()

    json.dump(record, open("./temp.json", "w", encoding='utf-8'))
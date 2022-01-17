from PIL import Image
from io import BytesIO
import requests
import numpy as np

# class RequestHandler():
#     def __init__(self):
#         pass

url = 'https://s9.mkklcdnv6tempv3.com/mangakakalot/v2/vy918232/chapter_57/1.jpg'
headers = {"referer":"https://readmanganato.com"}

response = requests.get(url, headers=headers)
print(dir(response))
image_data = response.content
print(type(image_data))
img = Image.open(BytesIO(image_data))
img.show()

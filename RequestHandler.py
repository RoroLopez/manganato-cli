from PIL import Image
from io import BytesIO
import requests

class RequestHandler():
    def __init__(self):
        # since none of the requests needs more than one header, we can separate them in a dict
        self.headers = {
            "host-name": "readmanganato.com",
            "id": "",
            "referer": "https://readmanganato.com"
        }

        self.endpoints = {
            "basic_info": "http://localhost:3000/manga_list",
            "chapters": "http://localhost:3000/manga_info",
            "read": "http://localhost:3000/read_manga",
            "jpg": ""
        }
    
    def basic_information(self, manga_name):
        return self.get(self.endpoints['basic_info'] + '?keyw=' + manga_name, headers=None)
    
    def get_chapters(self, manga_name):
        pass
    
    def read_manga(self, manga_name):
        pass
    
    def parse_chapters(self):
        pass
    
    def parse_information(self):
        pass
    
    def get(self, url, headers):
        return requests.get(url, headers=headers)
        

# url = 'https://s9.mkklcdnv6tempv3.com/mangakakalot/v2/vy918232/chapter_57/1.jpg'
# headers = {"referer":"https://readmanganato.com"}

# response = requests.get(url, headers=headers)
# print(dir(response))
# image_data = response.content
# print(type(image_data))
# img = Image.open(BytesIO(image_data))
# img.show()
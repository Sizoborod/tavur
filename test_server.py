import requests
import random

url = 'http://127.0.0.1:8080/file_upload'

name_file = f'static/img/id{random.randrange(1,3)}.jpg'
fp = open(name_file, 'rb')
coord = f'55.484{random.randrange(1000)},46.964{random.randrange(1000)}'


files = {'coord': coord,
         'text': 'Приятно познакомиться', 'file': fp}

resp = requests.post(url, files=files)
fp.close()
print(resp.text)

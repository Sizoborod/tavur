import requests

url = 'http://127.0.0.1:8080/file_upload'

fp = open('static/img/id1.jpg', 'rb')

files = {'coord': '12.123456,45.568899',
         'text': 'Приятно познакомиться', 'file': fp}

resp = requests.post(url, files=files)
fp.close()
print(resp.text)

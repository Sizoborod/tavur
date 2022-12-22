from flask import Flask, url_for, request, redirect
import datetime as dt
from PIL import Image
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'upload'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])






app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/file_upload', methods=['POST'])
def file_upload():
    request.encoding = 'UTF-8'
    if request.method == 'POST':
        coord = request.files['coord'].read().decode().split(',')
        text = request.files['text'].read().decode()
        f = request.files['file']
        my_date = dt.datetime.now()
        my_date = my_date.strftime("%Y-%m-%d_%H-%M-%S")
        name = f"upload/{my_date}.txt"
        d = open(name, mode="w", encoding='utf-8')
        print(f"{my_date}\n{coord[0]}\n{coord[1]}\n{text}", file=d)
        d.close()
        name_img = f"{my_date}.jpg"
        file = request.files['file']
        if file and allowed_file(file.filename):
            # filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], name_img))

        print(f.read())
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

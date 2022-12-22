from flask import Flask, url_for, request, redirect, render_template
import datetime as dt
from PIL import Image
import os
from werkzeug.utils import secure_filename
import flask_restful
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from waitress import serve
from werkzeug.utils import redirect

from flask_restful import reqparse, abort, Api, Resource

UPLOAD_FOLDER = 'static'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])




from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from waitress import serve
from werkzeug.utils import redirect

from flask_restful import reqparse, abort, Api, Resource



app = Flask(__name__)
api = flask_restful.Api(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'




@app.route('/')
def main_window():
    return render_template('object_manager.html')


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
        name = f"static/txt/{my_date}.txt"
        d = open(name, mode="w", encoding='utf-8')
        print(f"{my_date}\n{coord[0]}\n{coord[1]}\n{text}", file=d)
        d.close()
        name_img = f"img/{my_date}.jpg"
        file = request.files['file']
        if file and allowed_file(file.filename):
            # filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], name_img))

        print(f.read())
        return "Форма отправлена"




if __name__ == '__main__':
    '''app.run(port=8080, host='127.0.0.1')'''
    serve(app, host='0.0.0.0', port=5000)


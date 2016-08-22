import os
import json, base64
from flask import Flask, request, redirect, url_for, render_template, jsonify
from werkzeug.utils import secure_filename
from config import ALIYUN_CONFIG

#import aliyun openapi sdk
from com.aliyun.api.gateway.sdk import client
from com.aliyun.api.gateway.sdk.http import request as aliyun_request
from com.aliyun.api.gateway.sdk.common import constant

host = ALIYUN_CONFIG['HOST']
url = ALIYUN_CONFIG['URL']

cli = client.DefaultClient(app_key=ALIYUN_CONFIG['APP_KEY'], app_secret=ALIYUN_CONFIG['APP_SECRET'])

def post_data_to_aliyun(data):
    req_post = aliyun_request.Request(host=host, url=url, method="POST", time_out=30000)
    body = {}
    body["inputs"] = [
        {
            "image":{
                "dataType":50,
                "dataValue": data
            }
        }
    ]

    req_post.set_body(bytearray(source=json.dumps(body), encoding="utf8"))
    req_post.set_content_type(constant.CONTENT_TYPE_STREAM)
    req_post.set_protocol(constant.HTTPS)
    res_data = cli.execute(req_post)
    print res_data[2]
    return res_data[2]


UPLOAD_FOLDER = './static/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        base64_encoded_data = base64.b64encode(file.read())
        #print(base64_encoded_data)
        data_from_aliyun = post_data_to_aliyun(base64_encoded_data)


        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #return data_from_aliyun
            return data_from_aliyun
    return render_template('upload.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')

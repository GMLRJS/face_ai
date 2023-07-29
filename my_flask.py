from flask import Flask, request
from flask_cors.extension import CORS
from FACE_LOGIN3.face.make_folder import make_folder
from FACE_LOGIN3.face.pic2numpy import pic2num
from FACE_LOGIN3.face.make_h5 import make_h5
from FACE_LOGIN3.face.predict_for_login import predict
import os
from FACE_LOGIN3.face.dao_facelogin import DaoFacelogin
from flask.json import jsonify


app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = 'image/'


# @app.route('/')
@app.route('/capture.ajax', methods=['POST'])
def capture():
    mem_id = request.form.get('mem_id')  # ID 가져오기
    files = request.files.getlist('file[]')  # 사진 가져오기
    make_folder(mem_id) # ID로 폴더 만들기
    for f in files:
        f.save("mem_image/{}/".format(mem_id) + f.filename) # 폴더에 가져온 사진들 저장하기
        
    file_list = os.listdir("mem_image/{}/".format(mem_id)) # 사진들 파일명을 리스트로 받기
   
    pic2num(mem_id)
    make_h5(mem_id)
    
    return 'success'


@app.route('/login.ajax', methods=['POST'])
def login():
    mem_id = request.form.get('mem_id')  # ID 가져오기
    file = request.files.get('file')
    file.save("mem_image/{}/".format(mem_id) + file.filename)
    
    if predict(mem_id) == 1:
        df = DaoFacelogin()
        pw = df.selectPW(mem_id)[0]
        
        return pw
    else:
        return 'fail'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
    
    
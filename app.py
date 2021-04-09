# -*- coding:UTF-8 -*-
import flask
from flask import Flask, jsonify, json ,request
from server import *
import os ,shutil, base64, re

app = Flask(__name__)

@app.route('/')
def ree():
    pass

@app.route('/up', methods=['POST', 'GET'])
def up():
    if request.method == 'POST':
        bytes_data = request.get_data()
        json_data = str(bytes_data, 'utf-8')
        data = json.loads(json_data)
        img_id = data['img_id']
        img_list = data['img_bytes']

        path = "upload/"+img_id
        path1 = "upload/"+img_id+'/0'
        if os.path.exists(path):
            shutil.rmtree(path)
            os.mkdir(path)
        else:
            os.mkdir(path)
        if os.path.exists(path1):
            shutil.rmtree(path1)
            os.mkdir(path1)
        else:
            os.mkdir(path1)

        for name,value in img_list.items():
            with open(r'upload/'+img_id+'/'+'0/'+name+'.jpg','wb')as f:
                f.write(base64.b64decode(value))
        
        yy = transf(test(ds(path)))
        
        path2 = "upload/"+img_id+"/0"
        #图片名和识别结果合成字典
        xx = file_name(path2)
        
        ress = res(xx, yy)
        #删除文件
        shutil.rmtree(path)
            
        return json.dumps(ress,ensure_ascii=False)

if __name__ == '__main__':
   #app.run(processes=True)
   app.run(host='0.0.0.0', port=5050,debug=True,threaded = False,processes=1)
   app.config['JSON_AS_ASCII'] = False
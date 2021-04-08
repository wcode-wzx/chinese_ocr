from flask import Flask, jsonify, json ,request
from server import *
import os ,shutil, base64

app = Flask(__name__)

@app.route('/')
def re():
    re = "url/re 返回结果 "
    return re

@app.route('/up', methods=['POST', 'GET'])
def up():
    if request.method == 'POST':
        bytes_data = request.get_data()
        json_data = str(bytes_data, 'utf-8')
        data = json.loads(json_data)
        img_id = data['img_id']
        img_list = data['img_bytes']

        path = "upload/"+img_id
        if os.path.exists(path):
            shutil.rmtree(path)
            os.mkdir(path)
        else:
            os.mkdir(path)

        for name,value in img_list.items():
            with open(r'upload/'+img_id+'/'+name+'.jpg','wb')as f:
                f.write(base64.b64decode(value))
        
        yy = transf(test(ds('upload')))
        
        path = "upload/"+img_id
        #图片名和识别结果合成字典
        d = dict(zip(file_name(path), yy))
        #删除文件
        shutil.rmtree(path)
            
        return json.dumps(d,ensure_ascii=False)

if __name__ == '__main__':
   #app.run(processes=True)
   app.run(host='0.0.0.0', port=5050,debug=True,threaded = False,processes=1)
#    app.config['JSON_AS_ASCII'] = False
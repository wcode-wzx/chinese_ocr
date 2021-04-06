from flask import Flask, jsonify, json ,request
from server import *
import os ,shutil
app = Flask(__name__)
 
@app.route('/re')
def hello_world():    
    def file_name(file_dir):  
        L=[]  
        for root, dirs, files in os.walk(file_dir): 
            for file in files: 
                #if os.path.splitext(file)[1] == '.jpg': 
                L.append(file.split('.')[0]) 
        return L
    #返回识别结果
    yy = transf(test(ds('upload')))
    
    path = "upload\\1"
    #图片名和识别结果合成字典
    d = dict(zip(file_name(path), yy))
    #print(d)
    #(file_name(path),yy)
    #情况上传目录
    if os.path.exists(path):
        shutil.rmtree(path)
        os.mkdir(path)
    else:
        os.mkdir(path)
    
    return json.dumps(d,ensure_ascii=False)
    
@app.route('/up', methods=['POST', 'GET'])
def up():
    if request.method == 'POST':
        basepath = os.path.dirname(__file__)
        fs = request.files.getlist('file') # 一次性多个文件
        #print(fs)
        for f in fs:
            new_fname = os.path.join(basepath, 'upload\\1\\',f.filename)
            f.save(new_fname)
    response = {'msg':1}
    return jsonify(response)

if __name__ == '__main__':
   app.run(debug = True)
   app.config['JSON_AS_ASCII'] = False
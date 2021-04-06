from flask import Flask, jsonify, json, render_template,request,redirect,url_for
from server import *
from werkzeug.utils import secure_filename
import os ,shutil
app = Flask(__name__)
 
@app.route('/re')
def hello_world():
    
    #xx=os.listdir(r'E:\vsProject\YOLOv5\chinese_ocr\upload\0')
    yy = transf(test())
    path = "E:\\vsProject\\YOLOv5\\chinese_ocr\\upload\\1"
    if os.path.exists(path):
        shutil.rmtree(path)
        os.mkdir(path)
    else:
        os.mkdir(path)
    #d = dict(zip(xx, yy))
    #print(d)
    return json.dumps(yy,ensure_ascii=False)

@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname(__file__)  # 当前文件所在路径
        upload_path = os.path.join(basepath, 'upload\\',secure_filename(f.filename))  #注意：没有的文件夹一定要先创建，不然会提示没有该路径
        f.save(upload_path)
        return redirect(url_for('upload'))
        yy = transf(test())
    #d = dict(zip(xx, yy))
    #print(d)
    
    return render_template('upload.html')
    return json.dumps(yy,ensure_ascii=False)
    
@app.route('/up', methods=['POST', 'GET'])
def up():
    if request.method == 'POST':
        basepath = os.path.dirname(__file__)
        fs = request.files.getlist('file') # 一次性多个文件
        #fs = request.files['file']
        print(fs)
        for f in fs:
            new_fname = os.path.join(basepath, 'upload\\1\\',f.filename)
            f.save(new_fname)
    response = {'msg':1}
    return jsonify(response)

if __name__ == '__main__':
   app.run(debug = True)
   app.config['JSON_AS_ASCII'] = False
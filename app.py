from flask import Flask, jsonify, json
from server import *

app = Flask(__name__)

@app.route('/')
def hello_world():
    
    #xx=os.listdir(r'E:\vsProject\YOLOv5\chinese_ocr\upload\0')
    yy = transf(test())
    #d = dict(zip(xx, yy))
    #print(d)
    return json.dumps(yy,ensure_ascii=False)

if __name__ == '__main__':
   app.run(debug = True)
   app.config['JSON_AS_ASCII'] = False
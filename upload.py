import os, requests
 
url = 'http://192.168.1.14:5050/up'
#url = 'http://127.0.0.1:5000/up'

filePath = 'C:/Users/thyme/Desktop/1'

# for dirpath, dirnames, filenames in os.walk(filePath):
#     path = [os.path.join(dirpath, names) for names in filenames]
#     for xx in path:
import base64
for i in range(0,10):
    with open("C:/Users/thyme/Desktop/1/00.jpg", 'rb') as f:
        base64_data = base64.b64encode(f.read())
        s = base64_data.decode()
        #print(xx)
        #files = {'file': open(str(xx), 'rb'),}           
        a = {"img_id":str(i),"img_bytes":{"dsf":s}}
        #消息头指定
        headers = {'Content-Type': 'application/json;charset=UTF-8'}
        #发送post请求 json参数直接为一个字典数据。
        res = requests.request("post",url,json=a,headers=headers)
        print(res.status_code)
        print(res.text)
    # json = response.json()
    # print(json)

# re = requests.get(url+'re')
# json = re.json()
# print(json)

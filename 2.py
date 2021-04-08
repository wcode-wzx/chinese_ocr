import os, requests
import threading,time


filePath = 'C:/Users/thyme/Desktop/1'

# for dirpath, dirnames, filenames in os.walk(filePath):
#     path = [os.path.join(dirpath, names) for names in filenames]
#     for xx in path:
import base64

def run():
    url = 'http://127.0.0.1:5050/up'
    with open("C:/Users/thyme/Desktop/1/00.jpg", 'rb') as f:
        base64_data = base64.b64encode(f.read())
        s = base64_data.decode()
        #print(xx)
        #files = {'file': open(str(xx), 'rb'),}           
        a = {"img_id":"jadaho_kjs45","img_bytes":{"dsf":s}}
        #消息头指定
        headers = {'Content-Type': 'application/json;charset=UTF-8'}
        #发送post请求 json参数直接为一个字典数据。
        res = requests.request("post",url,json=a,headers=headers)
        print(res.status_code)
        print(res.text)

    # json = response.json()
    # print(json)
start_time=time.time()
t1=threading.Thread(target=run)
t2=threading.Thread(target=run)
t3=threading.Thread(target=run)
t4=threading.Thread(target=run)
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()
print(time.time()-start_time)
# # re = requests.get(url+'re')
# # json = re.json()
# # print(json)

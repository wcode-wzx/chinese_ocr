import os, requests
import threading,time
import base64

def run():
    filePath = 'C:/Users/thyme/Desktop/2'
    url = 'http://192.168.1.14:5050/up'
    #url = 'http://127.0.0.1:5050/up'
    list = []
    for dirpath, dirnames, filenames in os.walk(filePath):
        path = [os.path.join(dirpath, names) for names in filenames]
        for xx in path: 
            with open(xx, 'rb') as f:
                base64_data = base64.b64encode(f.read())
            a = base64_data.decode()
            xx = xx.split('\\')[-1].split('.')[0]
            list.append([xx,a])
    print(list[0][0])
    x = {"img_id":"jadaho_kjs45","img_bytes":{list[0][0]:list[0][1], list[1][0]:list[1][1],list[2][0]:list[2][1],list[3][0]:list[3][1],list[4][0]:list[4][1],list[5][0]:list[5][1]}}
    #消息头指定
    headers = {'Content-Type': 'application/json;charset=UTF-8'}
    #发送post请求 json参数直接为一个字典数据。
    res = requests.request("post",url,json=x,headers=headers)
    print(res.status_code)
    print(res.text)

    # json = response.json()
    # print(json)
start_time=time.time()
for i in range(2):
    t=threading.Thread(target=run)
    t.start()    

# t1=threading.Thread(target=run)
# t2=threading.Thread(target=run)
# t3=threading.Thread(target=run)
# t4=threading.Thread(target=run)
# t1.start()
# t2.start()
# t3.start()
# t4.start()
# t1.join()
# t2.join()
# t3.join()
# t4.join()
    print(time.time()-start_time)
# # re = requests.get(url+'re')
# # json = re.json()
# # print(json)

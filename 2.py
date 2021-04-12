import os, requests
import threading,time
import base64

url = 'http://192.168.1.21:5050/up'
#url = 'http://192.168.1.14:5050/up'
filePath = 'C:/Users/thyme/Desktop/1'

def run():

    
    list = []
    for dirpath, dirnames, filenames in os.walk(filePath):
        path = [os.path.join(dirpath, names) for names in filenames]
        for xx in path: 
            with open(xx, 'rb') as f:
                base64_data = base64.b64encode(f.read())
            a = base64_data.decode()
            xx = xx.split('\\')[-1].split('.')[0]
            list.append([xx,a])
    #print(list[0][0])

    x = {"img_id":"jadaho_kjs45","img_bytes":{list[a][0]:list[a][1] for a in range(0,7)}}
    #消息头指定
    headers = {'Content-Type': 'application/json;charset=UTF-8'}
    #发送post请求 json参数直接为一个字典数据。
    res = requests.request("post",url,json=x,headers=headers)
    print(res.status_code)
    print(res.text)

def run1():
    
   
    list = []
    for dirpath, dirnames, filenames in os.walk(filePath):
        path = [os.path.join(dirpath, names) for names in filenames]
        for xx in path: 
            with open(xx, 'rb') as f:
                base64_data = base64.b64encode(f.read())
            a = base64_data.decode()
            xx = xx.split('\\')[-1].split('.')[0]
            list.append([xx,a])
    #print(list[0][0])

    x = {"img_id":"6568","img_bytes":{list[a][0]:list[a][1] for a in range(0,7)}}
    #消息头指定
    headers = {'Content-Type': 'application/json;charset=UTF-8'}
    #发送post请求 json参数直接为一个字典数据。
    res = requests.request("post",url,json=x,headers=headers)
    print(res.status_code)
    print(res.text)

def run2():
    
    list = []
    for dirpath, dirnames, filenames in os.walk(filePath):
        path = [os.path.join(dirpath, names) for names in filenames]
        for xx in path: 
            with open(xx, 'rb') as f:
                base64_data = base64.b64encode(f.read())
            a = base64_data.decode()
            xx = xx.split('\\')[-1].split('.')[0]
            list.append([xx,a])
    #print(list[0][0])

    x = {"img_id":"54332","img_bytes":{list[a][0]:list[a][1] for a in range(0,7)}}
    #消息头指定
    headers = {'Content-Type': 'application/json;charset=UTF-8'}
    #发送post请求 json参数直接为一个字典数据。
    res = requests.request("post",url,json=x,headers=headers)
    print(res.status_code)
    print(res.text)

def run3():
    
    list = []
    for dirpath, dirnames, filenames in os.walk(filePath):
        path = [os.path.join(dirpath, names) for names in filenames]
        for xx in path: 
            with open(xx, 'rb') as f:
                base64_data = base64.b64encode(f.read())
            a = base64_data.decode()
            xx = xx.split('\\')[-1].split('.')[0]
            list.append([xx,a])
    #print(list[0][0])

    x = {"img_id":"3","img_bytes":{list[a][0]:list[a][1] for a in range(0,7)}}
    #消息头指定
    headers = {'Content-Type': 'application/json;charset=UTF-8'}
    #发送post请求 json参数直接为一个字典数据。
    res = requests.request("post",url,json=x,headers=headers)
    print(res.status_code)
    print(res.text)

def run4():
    
    list = []
    for dirpath, dirnames, filenames in os.walk(filePath):
        path = [os.path.join(dirpath, names) for names in filenames]
        for xx in path: 
            with open(xx, 'rb') as f:
                base64_data = base64.b64encode(f.read())
            a = base64_data.decode()
            xx = xx.split('\\')[-1].split('.')[0]
            list.append([xx,a])
    #print(list[0][0])

    x = {"img_id":"4","img_bytes":{list[a][0]:list[a][1] for a in range(0,7)}}
    #消息头指定
    headers = {'Content-Type': 'application/json;charset=UTF-8'}
    #发送post请求 json参数直接为一个字典数据。
    res = requests.request("post",url,json=x,headers=headers)
    print(res.status_code)
    print(res.text)

def run5():
   
    list = []
    for dirpath, dirnames, filenames in os.walk(filePath):
        path = [os.path.join(dirpath, names) for names in filenames]
        for xx in path: 
            with open(xx, 'rb') as f:
                base64_data = base64.b64encode(f.read())
            a = base64_data.decode()
            xx = xx.split('\\')[-1].split('.')[0]
            list.append([xx,a])
    #print(list[0][0])

    x = {"img_id":"5","img_bytes":{list[a][0]:list[a][1] for a in range(0,7)}}
    #消息头指定
    headers = {'Content-Type': 'application/json;charset=UTF-8'}
    #发送post请求 json参数直接为一个字典数据。
    res = requests.request("post",url,json=x,headers=headers)
    print(res.status_code)
    print(res.text)


def run6():
   
    list = []
    for dirpath, dirnames, filenames in os.walk(filePath):
        path = [os.path.join(dirpath, names) for names in filenames]
        for xx in path: 
            with open(xx, 'rb') as f:
                base64_data = base64.b64encode(f.read())
            a = base64_data.decode()
            xx = xx.split('\\')[-1].split('.')[0]
            list.append([xx,a])
    #print(list[0][0])

    x = {"img_id":"6","img_bytes":{list[a][0]:list[a][1] for a in range(0,7)}}
    #消息头指定
    headers = {'Content-Type': 'application/json;charset=UTF-8'}
    #发送post请求 json参数直接为一个字典数据。
    res = requests.request("post",url,json=x,headers=headers)
    print(res.status_code)
    print(res.text)

def run7():
   
    list = []
    for dirpath, dirnames, filenames in os.walk(filePath):
        path = [os.path.join(dirpath, names) for names in filenames]
        for xx in path: 
            with open(xx, 'rb') as f:
                base64_data = base64.b64encode(f.read())
            a = base64_data.decode()
            xx = xx.split('\\')[-1].split('.')[0]
            list.append([xx,a])
    #print(list[0][0])

    x = {"img_id":"7","img_bytes":{list[a][0]:list[a][1] for a in range(0,7)}}
    #消息头指定
    headers = {'Content-Type': 'application/json;charset=UTF-8'}
    #发送post请求 json参数直接为一个字典数据。
    res = requests.request("post",url,json=x,headers=headers)
    print(res.status_code)
    print(res.text)


def run8():
    
    list = []
    for dirpath, dirnames, filenames in os.walk(filePath):
        path = [os.path.join(dirpath, names) for names in filenames]
        for xx in path: 
            with open(xx, 'rb') as f:
                base64_data = base64.b64encode(f.read())
            a = base64_data.decode()
            xx = xx.split('\\')[-1].split('.')[0]
            list.append([xx,a])
    #print(list[0][0])

    x = {"img_id":"8","img_bytes":{list[a][0]:list[a][1] for a in range(0,7)}}
    #消息头指定
    headers = {'Content-Type': 'application/json;charset=UTF-8'}
    #发送post请求 json参数直接为一个字典数据。
    res = requests.request("post",url,json=x,headers=headers)
    print(res.status_code)
    print(res.text)
    # json = response.json()
    # print(json)
start_time=time.time()
# for i in range(3):
#     t=threading.Thread(target=run)
#     t.start()    

t1=threading.Thread(target=run)
t2=threading.Thread(target=run1)
t3=threading.Thread(target=run2)
t4=threading.Thread(target=run3)
t5=threading.Thread(target=run4)
t6=threading.Thread(target=run5)
t7=threading.Thread(target=run6)
t8=threading.Thread(target=run7)
t9=threading.Thread(target=run8)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
t9.join()

print(start_time-time.time())
# # re = requests.get(url+'re')
# # json = re.json()
# # print(json)

import os, requests
 
url = 'http://127.0.0.1:5050/'

filePath = 'C:/Users/thyme/Desktop/1'

for dirpath, dirnames, filenames in os.walk(filePath):
    path = [os.path.join(dirpath, names) for names in filenames]
    for xx in path:
        print(xx)
        files = {'file': open(str(xx), 'rb'),}           
        data = None
  
        response = requests.post(url+'up', files=files, data=data)
        json = response.json()
        print(json)

# re = requests.get(url+'re')
# json = re.json()
# print(json)

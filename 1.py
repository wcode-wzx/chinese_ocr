import os
filePath = 'C:\\Users\\thyme\\Desktop\\train\\0'
for dirpath, dirnames, filenames in os.walk(filePath):
    path = [os.path.join(dirpath, names) for names in filenames]
    for fileP in path:
        print(fileP)
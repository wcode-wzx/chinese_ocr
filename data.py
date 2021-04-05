import os         
file_dir = r"C:/Users\\thyme\\Desktop\\加密图片分类备份\\test\\一"
i = 1
a = os.walk(file_dir)
b = None
for root, dirs, files in os.walk(file_dir):  
    print(i)
    i += 1
    print(root) #当前目录路径  
    #print(dirs) #当前路径下所有子目录  
    #print(files) #当前路径下所有非目录子文件 
print(b)

# name = ['一', '七', '三', '上', '下', '不', '中', '九', '了', '二', '五', '低', '保', '光', '八', '公', '六', '养', '内', '冷', '副', '加', '动', '十', '只', '右', '启', '呢', '味', '和', '响', '四', '地', '坏', '坐', '外', '多', '大', '好', '孩', '实', '小', '少', '左', '开', '当', '很', '得', '性', '手', '排', '控', '无', '是', '更', '有', '机', '来', '档', '比', '油', '泥', '灯', '电', '的', '皮', '盘', '真', '着', '短', '矮', '硬', '空', '级', '耗', '自', '路', '身', '软', '过', '近', '远', '里', '量', '长', '门', '问', '雨', '音', '高']
# for i in range(0,len(name)):
#     print(i)
#     oldname = "E:\\vsProject\\YOLOv5\\chinese_ocr\\test\\"+str(name[i])
#     newname = "E:\\vsProject\\YOLOv5\\chinese_ocr\\test\\"+str(i)
#     print(oldname,newname)
#     os.rename(oldname,newname)

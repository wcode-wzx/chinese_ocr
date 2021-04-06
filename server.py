import  torch, os
from torch.autograd import Variable
import cv2 as cv
import numpy as np 
from PIL import Image
from torch.utils.data import DataLoader,Dataset
from torchvision import datasets
from torchvision import transforms #数据的原始处理
import torch.nn.functional as F
import time
'''
引用pt格式保存模型和权重，仅需加载from mnist import Net即可
'''
def ds(root):
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Resize((28,28)),
        transforms.Grayscale(), # 将图片转换为Tensor,归一化至[0,1]
        # transforms.Normalize(mean=[.5, .5, .5], std=[.5, .5, .5]) # 标准化至[-1,1]
    ])

    test_dataset = datasets.ImageFolder(root='upload',transform=transform) 
    test_loader = DataLoader(test_dataset, batch_size=10, shuffle=False, drop_last=False, num_workers=4) 
    return test_loader

class CnnModel(torch.nn.Module):
    def __init__(self):
        super(CnnModel, self).__init__()
        #cin = 1, cout = 10, kernel = 5
        self.conv1 = torch.nn.Conv2d(1, 10, kernel_size=5)
        #cin = 10, cout = 20, kernel = 5
        self.conv2 = torch.nn.Conv2d(10, 20, kernel_size=5)
        #kernel = 2 x 2
        self.pooling = torch.nn.MaxPool2d(2)
        #in = 320 , out = 90 分类
        self.fc = torch.nn.Linear(320, 180)
        self.fc1 = torch.nn.Linear(180, 90)

    def forward(self, x):
        #Flatten data from (n, 1, 28, 28) to (n, 784)
        batch_size = x.size(0)
        x = F.relu(self.pooling(self.conv1(x)))
        x = F.relu(self.pooling(self.conv2(x)))
        # view将矩阵转换为向量
        x = x.view(batch_size, -1)
        x = self.fc(x)
        x = self.fc1(x)
        return x

    def len(self, x):
        return len(self.fc1)

model = CnnModel()

#把计算迁移到GPU
# device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
# model.to(device)

def test(test_loader):
    correct = 0
    total = 0
    re = []
    if len(re)!=0:
        re = []
    for data in test_loader:
        inputs, target = data
        # inputs, target = inputs.to(device), target.to(device)
        new_m = torch.load('weight/best.pt', map_location='cpu')
        outputs = new_m(inputs)
        #outputs = model(inputs)
        #我们取概率最大的那个数作为输出
        _, predicted = torch.max(outputs.data, dim=1)
        #print(predicted)
        nn = predicted.tolist()
        #print("nn:", nn)
        for i in nn:
            re.append(i)
    #print("re", re)
    return re

def transf(re):
    name = ['一', '七', '五', '低', '保', '光', '八', '公', '六', '养',\
            '内', '冷', '三', '副', '加', '动', '十', '只', '右', '启',\
            '呢', '味', '和', '上', '响', '四', '地', '坏', '坐', '外',\
            '多', '大', '好', '孩', '下', '实', '小', '少', '左', '开',\
            '当', '很', '得', '性', '手', '不', '排', '控', '无', '是',\
            '更', '有', '机', '来', '档', '比', '中', '油', '泥', '灯',\
            '电', '的', '皮', '盘', '真', '着', '短', '九', '矮', '硬',\
            '空', '级', '耗', '自', '路', '身', '软', '过', '了', '近',\
            '远', '里', '量', '长', '门', '问', '雨', '音', '高', '二']
    ree = []
    if len(ree)!=0:
        ree = []
    for j in range(8, len(re)):
        j = re[int(j)]
        ree.append(name[j])
    #print(re,ree)
    return ree
    
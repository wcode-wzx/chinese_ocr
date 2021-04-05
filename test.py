import  torch, os
from torch.autograd import Variable
import cv2 as cv
import numpy as np 
from PIL import Image
from torch.utils.data import DataLoader,Dataset
from torchvision import datasets
from torchvision import transforms #数据的原始处理
from train import CnnModel
import time
'''
引用pt格式保存模型和权重，仅需加载from mnist import Net即可
'''
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Resize((28,28)),
    transforms.Grayscale(), # 将图片转换为Tensor,归一化至[0,1]
    # transforms.Normalize(mean=[.5, .5, .5], std=[.5, .5, .5]) # 标准化至[-1,1]
])

# class Mydataset(torch.utils.Data.Dataset):
#     def __init__(self,data_dir='train',transform=transform):
#         super().__init__()
#         self.data_dir=data_dir
#         self.transform=transform

#     def __len__(self):
#         return len(self.df)

#     def __getiem__(self,idex):
#         img_name,label=self.df[idex]
#         img_path=os.path.join(self.data_dir,img_name)
#         image=cv.imread(img_path)
#         if self.transform is not None:
#             image=self.transform(image)
#         return image,label        

# train = Mydataset()
test_dataset = datasets.ImageFolder(root='test1',transform=transform) 
test_loader = DataLoader(test_dataset, batch_size=10, shuffle=False, drop_last=False, num_workers=4) 

model = CnnModel()

#把计算迁移到GPU
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model.to(device)

def test():
    correct = 0
    total = 0
    with torch.no_grad():#不用算梯度
        for data in test_loader:
            inputs, target = data
            inputs, target = inputs.to(device), target.to(device)
            new_m = torch.load('weight/ocr.pt')
            outputs = new_m(inputs)
            #outputs = model(inputs)
            #我们取概率最大的那个数作为输出
            _, predicted = torch.max(outputs.data, dim=1)
            print(predicted)
            total += target.size(0)
            #计算正确率
            correct += (predicted == target).sum().item()
    print('Accuracy on test set: %d %% [%d/%d]' % (100 * correct / total, correct, total))

def p_in(path):
    im = Image.open(path).resize((28, 28))     #取图片数据
    im = im.convert('L')      #灰度图
    im_data = np.array(im)
    im_data = torch.from_numpy(im_data).float()
    im_data = im_data.view(1, 1, 28, 28)
    if torch.cuda.is_available():
        img = Variable(im_data).cuda()
    #img_cv_2 = np.transpose(tensor_cv.numpy(), (1, 2, 0))
    #读取保存的模型和参数
    new_m = torch.load('weight/best.pt')
    outputs = new_m(img)
    print(outputs[0])
    _, pred = torch.max(outputs, 1)
    nn = pred.tolist()
    #print(nn[0],type(nn[0]))
    
    names = name[nn[0]]
    return names

if __name__=='__main__':
    
    time_start=time.time()
    test()
    time_end=time.time()
    print('time cost',time_end-time_start,'s')
    
    #Accuracy on test set: 99 % [36491/36492]
    #time cost 2059.3131341934204 s
    #单张图片预测
    name = ['一', '七', '三', '上', '下', '不', '中', '九', '了', '二', '五', '低', '保', '光', '八', \
        '公', '六', '养', '内', '冷', '副', '加', '动', '十', '只', '右', '启', '呢', '味', '和', '响', \
        '四', '地', '坏', '坐', '外', '多', '大', '好', '孩', '实', '小', '少', '左', '开', '当', '很', \
        '得', '性', '手', '排', '控', '无', '是', '更', '有', '机', '来', '档', '比', '油', '泥', '灯', \
        '电', '的', '皮', '盘', '真', '着', '短', '矮', '硬', '空', '级', '耗', '自', '路', '身', '软', \
        '过', '近', '远', '里', '量', '长', '门', '问', '雨', '音', '高']
    #print('预测为:',p_in('images/4.jpg'))
    
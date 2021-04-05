import torch
from torch.utils.data import DataLoader
from torchvision import transforms #数据的原始处理
from torchvision import datasets
import torch.nn.functional as F
import torch.optim as optim
import numpy as np 
import matplotlib.pyplot as plt
#dataset

#我们拿到的图片是pillow,我们要把他转换成模型里能训练的tensor也就是张量的格式
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Resize((28,28)),
    transforms.Grayscale(), # 将图片转换为Tensor,归一化至[0,1]
    #transforms.Normalize(mean=[.5], std=[.5]), # 标准化至[-1,1]
])
train_dataset = datasets.ImageFolder(root='train',transform=transform) 
train_loader = DataLoader(train_dataset, batch_size=10, shuffle=True, drop_last=False, num_workers=4) 
test_dataset = datasets.ImageFolder(root='train',transform=transform) 
test_loader = DataLoader(test_dataset, batch_size=10, shuffle=True, drop_last=False, num_workers=4) 

#计算均值和方差
def get_mean_std(dataset, ratio=0.01):
    """Get mean and std by sample ratio
    """
    dataloader = torch.utils.data.DataLoader(dataset, batch_size=int(len(dataset)*ratio), 
                                             shuffle=True, num_workers=4)
    train = iter(dataloader).next()[0]   # 一个batch的数据
    mean = np.mean(train.numpy(), axis=(0,2,3))
    std = np.std(train.numpy(), axis=(0,2,3))
    return mean, std


#model.farward
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
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model.to(device)

#opt.loss

#定义一个损失函数，来计算我们模型输出的值和标准值的差距
criterion = torch.nn.CrossEntropyLoss()
#定义一个优化器，训练模型咋训练的，就靠这个，他会反向的更改相应层的权重
optimizer = optim.SGD(model.parameters(),lr=0.1,momentum=0.5)#lr为学习率

#training update
xxx = []
yyy = []
def train(epoch):
    running_loss = 0.0
    for batch_idx, data in enumerate(train_loader, 0):#每次取一个样本
        inputs, target = data
        #print("inputs:", inputs, inputs.size(),"target:", target)
        inputs, target = inputs.to(device), target.to(device)
        #优化器清零
        optimizer.zero_grad()
        # 正向计算一下
        outputs = model(inputs)
        #计算损失
        loss = criterion(outputs, target)
        #反向求梯度
        loss.backward()
        #更新权重
        optimizer.step()
        #把损失加起来
        running_loss += loss.item()
        #每300次输出一下数据
        if batch_idx % 5 == 4:
            print('[%d, %5d] loss: %.8f' % (epoch + 1, batch_idx + 1, running_loss / 2000))
            yyy.append(running_loss)
            running_loss = 0.0
    

#test
def test():
    correct = 0
    total = 0
    with torch.no_grad():#不用算梯度
        for data in test_loader:
            inputs, target = data
            inputs, target = inputs.to(device), target.to(device)
            outputs = model(inputs)
            #我们取概率最大的那个数作为输出
            _, predicted = torch.max(outputs.data, dim=1)
            total += target.size(0)
            #计算正确率
            correct += (predicted == target).sum().item()
    print('Accuracy on test set: %d %% [%d/%d]' % (100 * correct / total, correct, total))


if __name__=='__main__':
    for epoch in range(5):
        train(epoch)
        test()
    torch.save(model, 'ocr.pt') 
    #test()
    
    for iii in range(len(yyy)):
        xxx.append(iii)
    plt.plot(xxx, yyy)
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.show()
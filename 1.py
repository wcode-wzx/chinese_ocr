from torchvision import transforms #数据的原始处理
from torchvision import datasets
from torch.utils.data import DataLoader,Dataset


transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Resize((28,28)),
        transforms.Grayscale(), # 将图片转换为Tensor,归一化至[0,1]
        # transforms.Normalize(mean=[.5, .5, .5], std=[.5, .5, .5]) # 标准化至[-1,1]
    ])

test_dataset = datasets.ImageFolder(root='upload',transform=transform) 


print(test_dataset.imgs,type(test_dataset))

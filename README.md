# 单个文字识别分类api

# linux环境下部署
- 由于系统影响读取文件名称的顺序，在linux系统上需要对结果进行转化，server.py ree() 函数进行重新排序即可

## 在项目文件夹下执行如下操作

- 创建虚拟环境
- python3 -m venv .venv
- 激活
- source .venv/bin/activate
- 安装环境
- pip ...Flask

# torch 安装

pip install torch==1.8.1+cpu torchvision==0.9.1+cpu torchaudio==0.8.1 -f https://download.pytorch.org/whl/torch_stable.html



nohup python -u app.py > test.log 2>&1 &


import re

def res(xx, yy):
    x1 = xx[0][0:3] 
    list = []
    list2 = []
    for i in range(0,len(xx)):
        list.append(int(xx[i][3:7],16))
    list.sort()
    for j in list:
        list2.append(x1+hex(j).upper()[2:6])
    re = dict(zip(list2, yy))
    return re
    print(list,list2,x1,re)
xx = ['uniEE0A', 'uniEE02', 'uniEE0B', 'uniEE04']
yy = ['呢', '冷', '不', '和']

print(res(xx, yy))
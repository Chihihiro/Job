#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/1/7 0007 10:20 
# @Author : Chihiro 
# @Site :  
# @File : p1.py 
# @Software: PyCharm


import matplotlib.pyplot as plt
GDP = [12406.8,13908.57,9386.87,9143.64]
plt.rcParams['font.sans-serif'] =['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
plt.bar(range(4), GDP, align = 'center',color='steelblue', alpha = 0.8)
plt.ylabel('GDP')
plt.title('四个直辖市GDP大比拼')
plt.xticks(range(4),['北京市','上海市','天津市','重庆市'])
plt.ylim([5000,15000])
for x,y in enumerate(GDP):
    plt.text(x,y+100,'%s' %round(y,1),ha='center')
# 显示图形
plt.show()

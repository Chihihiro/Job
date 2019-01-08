#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/1/8 0008 9:47 
# @Author : Chihiro 
# @Site :  
# @File : p2.py 
# @Software: PyCharm

import matplotlib.pyplot as plt

plt.style.use('ggplot')

edu = [0.2515, 0.3724, 0.3336, 0.0368, 0.0057]
labels = ['Secondary', 'Junior College', 'Bachelor', 'Master', 'Others']

explode = [0, 0.1, 0, 0, 0]
colors = ['#FEB748', '#EDD25D', '#FE4F54', '#51B4FF', '#dd5555']

# 中文乱码和坐标轴负号的处理
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

# 将横、纵坐标轴标准化处理，保证饼图是一个正圆，否则为椭圆
plt.axes(aspect='equal')

# 控制x轴和y轴的范围
plt.xlim(0, 4)
plt.ylim(0, 4)

plt.pie(x=edu, explode=explode, labels=labels, colors=colors,
        autopct='%.1f%%', pctdistance=0.8, labeldistance=1.15, startangle=180,
        radius=1.5, counterclock=False, wedgeprops={'linewidth': 1.5, 'edgecolor': 'green'},
        textprops={'fontsize': 12, 'color': 'k'}, center=(1.8, 1.8), frame=1)
# 绘图数据
# 突出显示大专人群
# 添加教育水平标签设置饼图的自定义填充色
# 设置百分比的格式，这里保留一位小数      # 设置百分比标签与圆心的距离      
# 设置教育水平标签与圆心的距       
# 设置饼图的初始角度      
# 设置饼图的半       
# 是否逆时针，这里设置为顺时针方   
# 设置饼图内外边界的属性值     
# 设置文本标签的属性值   
# 设置饼图的原点
# 是否显示饼图的图框，这里设置显示
# 删除x轴和y轴的刻度
plt.xticks(())
plt.yticks(())
# 添加图标题
plt.title('Zhima Credit Discredited User Analysis')

plt.show()

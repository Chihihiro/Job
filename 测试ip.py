#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2018/12/29 0029 15:00 
# @Author : Chihiro 
# @Site :  
# @File : 测试ip.py 
# @Software: PyCharm

from telnetlib import Telnet


def ip_test(ip, port):
    try:
        Telnet(ip, port)
    except:
        return False
    else:
        return True


i = {"code":"0","msg":[{"port":"20097","ip":"183.154.49.148"},{"port":"40720","ip":"114.226.91.2"},{"port":"23399","ip":"59.32.47.235"},{"port":"46952","ip":"121.239.123.36"},{"port":"26312","ip":"117.87.186.8"},{"port":"36256","ip":"1.28.0.145"},{"port":"21899","ip":"115.213.101.59"},{"port":"20565","ip":"101.205.146.181"},{"port":"38752","ip":"125.122.118.119"},{"port":"31962","ip":"125.118.73.169"}]}

ips = i["msg"]

for ip in ips:
    print(ip_test(ip["ip"], ip["port"]))

# print(ip_test(
#     "49.68.68.197", "33220"
# ))


#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 2019/1/8 0008 13:07 
# @Author : Chihiro 
# @Site :  
# @File : 练习.py 
# @Software: PyCharm

# Selenium模拟拖动网页
#
# 1.JavaScript = ECMAScript   +   DOM  +  BOM
# ECMAScript标准(ECAM组织):  定义了JavaScript的核心语法
# DOM(W3C):  专门操作网页内容的API
# BOM:  专门操作浏览器窗口的API
#
# Selenium点掉弹框
# browser.switch_to.alert.accept()
#
# JS实现拖拽网页
# window.scroll(x,y)
#
# Selenium执行js脚本
# browser.execute_script(js代码)
#
# Selenium获取网页源代码(渲染之后)
# browser.page_source
#
# PhantomJS
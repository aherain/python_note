# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 15:35:51 2019

@author: fengxianhegui
"""
# 网络请求包
import requests
#html 解析器
import lxml
#网页筛选器 它能解析html代码并且从代码中提取我们想要的数据
from bs4 import BeautifulSoup  as bs
#正则表达式
import re


#获取网页上的所有数据
url = 'http://www.cbirc.gov.cn/cn/list/9103/910305/ybjjcf/1.html'
header = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
          'Accept-Encoding': 'gzip, deflate, sdch', 'Accept-Language': 'zh-CN,zh;q=0.8', 'Connection': 'keep-alive',
          'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
p1='行政处罚'

reponse = requests.get(url,headers =header).text
soup = bs(reponse,'lxml')

#通过CSS标签，找到对应的表格区域
data_list=soup.select('.table-fixed .zwbg-2')
# print(data_list)
#遍历找到的表格的每一行
for td in data_list:
    print('http://www.cbirc.gov.cn{}:{}'.format(td.a['href'], td.text))


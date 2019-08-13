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

的同学，直接使用这一杀器！
这是我与其它知友大群群主合作的运营工具，已经在其它群正式使用一段时间了，
反馈极好，互盘启动一般都能快速拿到30+的启动点数。

这是一个火狐浏览器下的插件，需要电脑安装火狐浏览器和水熊插件，安装、使用、说明请移步下面的链接查看详情
这里有非常详尽的说明，大家一定仔细阅读
http://shuixiong.awesometiny.com/doc

因为平台的开发和运维确实会造成一些成本，
所以功能的使用会收一点费用。
我们把收费压缩到50元一个月，就是希望不要给大家带来
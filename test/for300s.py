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
url = 'https://www.gushiwen.org/gushi/tangshi.aspx'
header = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
          'Accept-Encoding': 'gzip, deflate, sdch', 'Accept-Language': 'zh-CN,zh;q=0.8', 'Connection': 'keep-alive',
          'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
p1='行政处罚'

reponse = requests.get(url, headers=header).text
soup = bs(reponse,'lxml')

#通过CSS标签，找到对应的表格区域
data_list=soup.select('.table-fixed .zwbg-2')
# print(data_list)
#遍历找到的表格的每一行
for td in data_list:
    print('http://www.cbirc.gov.cn{}:{}'.format(td.a['href'], td.text))


# 逆概率问题，让贝叶斯大红大紫。
# 三百首诗词的爱恨情仇

#研读cef框架
bpm pload 下载程序相关的文件包：
tar finder init!
zip finder init!

开始加载eui的框架引导文件，引入了包文件：eui_win32:
[EUI] CEF Python 57.0
[EUI] Python 3.6.1 32bit


调用窗口创建程序：Window

NewWindow$ 2098552
2560 1377
NewMASK$ 4916354
NewINFO$ 2360590

调用：proc_win：
WinActive! 2098552


调用eui_win32中的对应方法：
OnBeforeBrowse 初始化内置函数


启动_OnContextCreated
绑定ExecuteJavascript 请求，渲染js




OnBeforeBrowse

1，第一步获取请求的url
ParseResult(
    scheme='http',
    netloc='223694672.statistics.wsgi',
    path='/assets/setting.png',
    params='', query='',
    fragment='')

2，实例化netloc='225791856.login.wsgi' 对应的 login.py 文件中的js 方法
   实例化到cef中的jsObject中，及默认的内置方法



2，获取实例中的全局信息中的用户信息user
# getApplication().user

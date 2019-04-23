#怎么连接NC新的数据库
import cx_Oracle                                          #引用模块cx_Oracle
import os, sys

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
conn=cx_Oracle.connect('jh/jh@10.30.1.40:1521/orcl')    #连接数据库
c=conn.cursor()                                           #获取cursor
#x=c.execute('select * from DBWZ20181226.VIEW_GLDETAIL')  #使用cursor进行各种操作
#x=c.execute('select * from DBWZ20181226.VIEW_GLVOUCHER')  #使用cursor进行各种操作
#r = x.fetchone()
print(c.execute('show table'))
c.close()                                                 #关闭cursor
conn.close()
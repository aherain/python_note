from requests import Request, Session

s = Session()
req = Request('GET', url,
    data=data,
    headers=header
)
prepped = req.prepare()

# do something with prepped.body
# do something with prepped.headers

resp = s.send(prepped,
    stream=stream,
    verify=verify,
    proxies=proxies,
    cert=cert,
    timeout=timeout
)

print(resp.status_code)

一个小想法
用工具包的方式二次封装一系列的方法
只需要传入数据
生成系列报告

提供编辑页面

包的使用说明 提交到git仓库管理维护

from docx import Document
from docx.shared import Inches
from PIL import Image

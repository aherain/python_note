__all__ = ['send', 'receive']
print("你导入的msg包%s" % ','.join(__all__))
def test():
    print("这里是msg包里面的test")


#打包
from distutils.core import setup
setup(name = "Se7eN_HOU",version = "1.0",description = "Se7eN_HOU's module",author = "Se7eN_HOU",py_modules = ["sub_A.a","sub_B.b"])
#同目录下执行python setup.py sdist


#解压和安装

# 找到模块的压缩包
# 解压  tar -zxvf java.tar.gz
# 进入文件夹
# 执行命令python setup.py install
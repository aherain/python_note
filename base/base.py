a = [66.25, 333, 333, 1, 1234.5]
print(a.count(66.25), a.count(333))

squares = list(map(str, range(10)))

print(squares)
squares = [x**2 for x in range(10)]
print(squares)

string1, string2, string3 = '', 1, 'Hammer Dance'
non_null = string1 or string2 or string3
print(non_null)

for x in range(1, 11):
    print('{0: 2d} {1: 3d} {2: 4d}'.format(x, x*x, x*x*x))


print('We are the {} who say "{}!"'.format('knights', 'Ni', 'hhhh'))


table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))


# glob 模块提供了一个函数用于从目录通配符搜索中生成文件列表:
import glob
a = glob.glob('*.py')
print(a)

# 以下模块直接支持通用的数据打包和压缩格式：zlib， gzip， bz2， lzma， zipfile 以及 tarfile。
import zlib
s = b'witch which has which witches wrist watch'
print(len(s))
t = zlib.compress(s)
print(t)
print(len(t))
print(zlib.decompress(t))

print(zlib.crc32(s))


# 相对于 timeit 的细粒度，profile 和 pstats 模块提供了针对更大代码块的时间度量工具。

# unittest 模块不像 doctest 模块那么容易使用，不过它可以在一个独立的文件里提供一个更全面的测试集:

# xmlrpc.client 和 xmlrpc.server 模块让远程过程调用变得轻而易举。尽管模块有这样的名字，用户无需拥有 XML 的知识或处理 XML。
#
# email 包是一个管理邮件信息的库，包括MIME和其它基于 RFC2822 的信息文档。
#
# 不同于实际发送和接收信息的 smtplib 和 poplib 模块，email 包包含一个构造或解析复杂消息结构（包括附件）及实现互联网编码和头协议的完整工具集。
#
# xml.dom 和 xml.sax 包为流行的信息交换格式提供了强大的支持。同样， csv 模块支持在通用数据库格式中直接读写。
#
# 综合起来，这些模块和包大大简化了 Python 应用程序和其它工具之间的数据交换。
#
# 国际化由 gettext， locale 和 codecs 包支持


import zipfile


def test1():
    for i in range(1, 4):
        f = open("file" + str(i) + ".txt", 'w')
        f.write(str(i))
        f.close()

    f = zipfile.ZipFile('filename.zip', 'w', zipfile.ZIP_DEFLATED)
    f.write('file1.txt')
    f.write('file2.txt')
    f.write('file3.txt')
    f.close()

    f = zipfile.ZipFile('filename.zip')
    f.extractall()
    f.close()


def test2():
    # 判断是不是压缩文件
    print(zipfile.is_zipfile('filename.zip'))

    # 文件列表
    f = zipfile.ZipFile('filename.zip')
    print(f.namelist())  # ['file1.txt', 'file2.txt', 'file3.txt']
    print(f.infolist())  # [<zipfile.ZipInfo object at 0x7fdcfddd0438>, <zipfile.ZipInfo object at 0x7fdcfddd0500>, <zipfile.ZipInfo object at 0x7fdcfddd0370>]
    print(f.getinfo('file1.txt'))  # <zipfile.ZipInfo object at 0x7fdcfddd0438>


if __name__ == "__main__":
    test2()

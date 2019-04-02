import marshal
fd = open('path/to/my.pyc', 'rb')
magic = fd.read(4) # 魔术数，与python版本相关
date = fd.read(4) # 编译日期
code_object = marshal.load(fd)
fd.close()

#文本分析bosonnlp:
# https://bosonnlp.com/demo#overview-ner
# http://docs.bosonnlp.com/sentiment.html


# Paoding（准确率、分词速度、新词识别等，最棒）
# jieba 结巴分词
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

#996.icu不是造反，是对美好生活点的向往
# 习大大：“我国社会主要矛盾已经转化为人民日益增长的美好生活需要和不平衡不充分的发展之间的矛盾”
# 一语道破，996.icu 事件的本质，它不是造反，它是社会矛盾的一种体现，是人民对美好生活的强烈需求，
# 我们需要冷静理性的看到，不夸大不弯曲，不回避敢面对，寻求最好的解决办法不能打压掩盖，这关系的是祖国的
# 发展和人民幸福。人民的事就是大事。

# 事件回顾：
# 3天破10w关注
# 登封reban

#舆情分析
#技术号集体转发，很开
#工资待遇金和美好的生活

# 历史的镜子
# 100年，需要给我们的祖国一些时间

# #蒙蒙，怎么就领饭盒了呢？
# 用http://docs.bosonnlp.com/sentiment.html
# 珀森神經網絡做文本分析。

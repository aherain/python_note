import marshal
fd = open('path/to/my.pyc', 'rb')
magic = fd.read(4) #魔术数，与python版本相关
date = fd.read(4) #编译日期
code_object = marshal.load(fd)
fd.close()

#文本分析bosonnlp:
# https://bosonnlp.com/demo#overview-ner
# http://docs.bosonnlp.com/sentiment.html


# Paoding（准确率、分词速度、新词识别等，最棒）
# jieba 结巴分词


#科学的两个必须：可重复，可预测

#可重复代表的是一项科学成果是可以推广和普适的应用
#可预测突显一个科学成果消除未来不确定性的信息价值
# http://www.ruanyifeng.com/blog/2015/06/poisson-distribution.html

# 辛普森悖论，你的选择有误区

#北上广择偶标准，精华版
# 1，总体描述：性别，年龄，身高，收入，学历，相貌，兴趣爱好，喜欢（评论）人数
# 聚类分析（物以类聚），对应分析（门当户对）
# 2，女生看重什么
# 3，男生看重什么


import os
import os.path
import pickle

def sheet_reader(filename):
    file = open(filename, mode='rb', encoding=None)
    file.seek(0)
    try:
        while True:
            block = pickle.load(file)
            for _ in block:
                yield _

    except EOFError:
        raise StopIteration

ar = 0
for row in sheet_reader("/data/dev_tongji_files/044/044015/sheet_44015"):
    ar = ar + row['revenue']

print('文件中的总票房', ar)


#向量的点积，交叉积；坐标是一种解析模型， 还有一种向量模型
#向量的线性组合，内积，叉积，线性变换等等的运算全部是坐标无关的
#集合论

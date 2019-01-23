
#使用模块
#使用装饰器
#使用类
#多线程模式下单例模式会出问题，需要加锁解决
#多线程实现单例模式
#基于metaclass元类的方式实现
import threading
class Singleton(object):
    _instance_lock = threading.Lock()

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):
            with Singleton._instance_lock:
                if not hasattr(Singleton, "_instance"):
                    Singleton._instance = object.__new__(cls)
        return Singleton._instance

obj1 = Singleton()
obj2 = Singleton()
print(obj1,obj2)

def task(arg):
    obj = Singleton()
    print(obj)

for i in range(10):
    t = threading.Thread(target=task,args=[i,])
    t.start()

def print_directory_contents(spath):
    import os
    for child in os.listdir(spath):
        scpath = os.path.join(spath, child)
        if os.path.isdir(scpath):
            print_directory_contents(scpath)
        else:
            print(scpath, '\n')

a0 = dict(zip(('a', 'b', 'c', 'd', 'e'), (1, 2, 3, 4, 5)))
print(a0)
a1 = range(10)
print(a1)
a2 = [i for i in a1 if i in a0]
print(a2)

a3 = [a0[s] for s in a0]
print(a3)

a4 = [i for i in a1 if i in a3]
print(a4)

a5 = {i: i*i for i in a1}
print(a5)
a6 = [[i, i*i] for i in a1]
print(a6)


def f(x, l=[]):
    for i in range(x):
        l.append(i*i)

    print(l)

# f(2)  #0,1
# f(3, [3,2,1]) #[3,2,1,0,1,4]
# f(3) #[0,1,0,1,4]
# #
# a
# a b
# a c
# b c d = a b c d #有重复的类不添加该类
# b c e = a b c  #有重复的类不添加该类


def f1(lIn):
    l1 = sorted(lIn)
    l2 = [i for i in l1 if i<0.5]
    return [i*i for i in l2]

def f2(lIn):
    l1 = [i for i in lIn if i<0.5]
    l2 = sorted(l1)
    return [i*i for i in l2]

def f3(lIn):
    l1 = [i*i for i in lIn]
    l2 = sorted(l1)
    return [i for i in l1 if i<(0.5*0.5)]

import random
import cProfile
lIn = [random.random() for i in range(100000)]
cProfile.run('f1(lIn)')
cProfile.run('f2(lIn)')
cProfile.run('f3(lIn)')


class A(object):
    def show(self):
        print('base show')

class B(A):
    def show(self):
        print('self show')

obj = B()
obj.show()

obj.__class__ = A
obj.show()


class C(object):
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def myprint(self):
        print('a=', self.__a, 'b=', self.__b)

    def __call__(self, num):
        print('call ', sum([num, self.__a]))

c1 = C(10, 20)
c1.myprint()

c1(80)


class D(object):
    def fn(self):
        print('D fn')

    def __init__(self):
        print('B INIT')

class E(object):
    def fn(self):
        print('E fn')

    def __new__(cls, a):
        print('NEW', a)
        if a > 10:
            return super(E, cls).__new__(cls)
        return D()

    def __init__(self, a):
        print('INIT', a)

d1 = E(5)
d1.fn()

d2 = E(20)
d2.fn()

class F(object):
    def __init__(self, a, b):
        self.a1 = a
        self.b1 = b
        print('init')

    def mydefault(self, *args):
        print('default: ' + str(args[0]))

    def __getattr__(self, name):
        print("other fn:", name)
        return self.mydefault

f1 = F(10, 20)
f1.fn1(33)
f1.fn2('hello')
f1.fn3(10)



def mulby(num):
    def gn(val):
        return num*val

    return gn

zw = mulby(7)
print(zw(9))

D = {'a': 1, 'b': 2, 'c': 3}
print(D.items())

for cell in D.items():
    print(cell)

# Removed dict.iteritems(), dict.iterkeys(), and dict.itervalues().
# Instead: use dict.items(), dict.keys(), and dict.values() respectively.
# for k, v in D.iteritems():
#     print(k, v)

def fibs(x):
    result = [0, 1]
    for index in range(x-2):
        result.append(result[-2]+result[-1])
    return result

print(fibs(5))

#python 简洁 明了 严谨 灵活
# if __name__ == '__main__':
#     print_directory_contents('c:\workcode\PL\\base')

# 结算类型：任务名称
# --------------------------------
# 最终结算：大雪冬至   #项目名称
# 快速结算：2018年5月快速结算  #按月份
# 分次结算：2018年6月《忌日快乐》分次结算 #月份项目名称分次结算
# 60天结算：2018年6月《21克拉》60天结算 #月份项目名称分次结算
# 预结算：
# 投资结算：
# 二级市场结算：2018年11月二级市场结算  #月份


#青松月结导入匹配院线
#select `name`,`chain` from uni_name_chains where usetype = 6
#上传
#凭风好借力，送我上青云
#数据分析方法汇总
# 一、描述性统计
# 二、回归分析
# 三、方差分析
# 四、假设检验
# 五、相关分析
# 六、聚类分析
# 七、判别分析
# 八、因子分析
# 九、主成分分析
# 十、列联表分析
# 十一、信度分析
# 十二、时间序列分析
# 十三、生存分析
# 十四、典型相关分析
# 十五、R0C分析
# 十六、其他分析方法
# 多重响应分析、距离分祈、
# 项目分祈、对应分祈、决策树分析、
# 神经网络、系统方程、蒙特卡洛模拟等




# 看数据分布
# 直方图 经验分布图 ecdf(x)生成向量
# 理想曲线，QQ图
#孩子们的游戏

# 数据分析的主旨，一直是发掘数据中的有价值的信息，更进一步是将信息转换为知识，最难的是将知识升华为洞见
# 参数 VS 统计量：用来描述总体特性的测量数称为总体的参数，而用来描述样本特性的测量数称为样本统计量
# 推断统计学一般有两种方法，一是使用置信区间估算总体的参数，二是对总体参数的假设值进行决策。后者被称为假设检验，是我们这篇文章所要探讨的主题。
#蒙特卡洛模拟 样本均值检验


#finalsettlement_get_cfm_data_by_stl
#finalsettlement_get_cfm_data_by_stl


#修理最终结算表中的数据
#有问题的结算表






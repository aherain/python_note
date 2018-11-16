import time
import inspect
class Test(object):
    def __init__(self):
        self.lis = [m for m in dir(self)]
    def dothis(self,nihao:str='123', aa:int='777'):
        print(self.lis)

        return

if __name__ == '__main__':
    ts = Test()
    print(str(ts.dothis))
    print("反射",inspect.getfullargspec(ts.dothis).annotations)
    ts.dothis('nihao', 'nihao')
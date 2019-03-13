class A:
    def __init__(self):
        self.n = 2

    def add(self, m):
        print('self is {0} @A.add'.format(self))
        print("aaaa", self.n)
        self.n += m
        print('aaaddd', self.n)


class B(A):
    def __init__(self):
        self.n = 3

    def add(self, m):
        print('self is {0} @B.add'.format(self))
        super().add(m)
        self.n += 3


b = B()
b.add(2)
print(b.n)

# python3 是广度优先
# python2 是深度优先
class CashSuper(object):
    def AcceptCash(self, money):
        return 0

class CashNormal(CashSuper):
    def AcceptCash(self, money):
        return money

class CashRebate(CashSuper):
    discount = 0
    def __init__(self, ds):
        self.discount = ds

    def AcceptCash(self, money):
        return money * self.discount

class CashReturn(CashSuper):
    total = 0
    ret = 0
    def __init__(self, t, r):
        self.total = t
        self.ret = r

    def AcceptCash(self, money):
        if money >= self.total:
            return money - self.ret
        else:
            return money

class CashContext:
    def __init__(self, csuper):
        self.cs = csuper

    def GetResult(self, money):
        return self.cs.AcceptCash(money)

if __name__ == "__main__":
    money = float(input("money"))

    strategy = {1: CashContext(CashNormal()),
                2: CashContext(CashRebate(0.8)),
                3: CashContext(CashReturn(300, 100))}

    ctype = input('settle way 1,2,3')

    cc = strategy.get(int(ctype), '')
    if cc:
        print(cc.GetResult(money))


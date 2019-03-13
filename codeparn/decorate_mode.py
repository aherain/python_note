class Person:
    def __init__(self, name):
        self.name = name
    def show(self):
        print("dressed the %s" % self.name)

class Finery(Person):
    componet = None
    def __init__(self):
        pass
    def decorate(self, ct):
        self.componet = ct

    def show(self):
        if self.componet:
            self.componet.show()


class Tshirt(Finery):
    def __init__(self):
        pass
    def show(self):
        print("Big shirt")
        self.componet.show()

class BigTrouser(Finery):
    def __init__(self):
        pass
    def show(self):
        print("big trouser")
        self.componet.show()


if __name__ == "__main__":
    p = Person('somebody')
    bt = BigTrouser()
    ts = Tshirt()
    bt.decorate(p)
    ts.decorate(bt)
    ts.show()
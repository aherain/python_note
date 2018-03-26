class Leifeng:
    def sweep(self):
        print("leifeng sweep")

class Student(Leifeng):
    def sweep(self):
        print("student sweep")

class Volenter(Leifeng):
    def sweep(self):
        print("volenter sweep")

class LeifengFactory:
    def createLeifeng(self):
        temp = Leifeng()
        return temp

class StudentFactory(LeifengFactory):
    def createLeifeng(self):
        temp = Student()
        return temp

class VolenterFactory(LeifengFactory):
    def createLeifeng(self):
        temp = Volenter()
        return temp

if __name__ == '__main__':
    sf = StudentFactory()
    s = sf.createLeifeng()
    s.sweep()

    sdf = VolenterFactory()
    s = sdf.createLeifeng()
    s.sweep()



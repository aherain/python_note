class Operation:
    def GetResult(self):
        pass

class OperationAdd(Operation):
    def GetResult(self):
        return self.op1 + self.op2

class OperationSub(Operation):
    def GetResult(self):
        return self.op1 - self.op2


class OperationMul(Operation):
    def GetResult(self):
        return self.op1 * self.op2


class OperationDiv(Operation):
    def GetResult(self):
        return  ('self.op2 is zero ' if self.op2==0 else self.op1 / self.op2)

class OperationUndef(Operation):
    def GetResult(self):
        print("undefined the operation")


class OperationFactory:

    operation = {'+': OperationAdd(),
                 '-': OperationSub(),
                 '*': OperationMul(),
                 '/': OperationDiv()}
    def createOption(self, ch):
        return self.operation.get(ch, OperationUndef())


if __name__ == "__main__":

    op = input("operation:")
    opa = input('a=')
    opb = input('b=')

    factory = OperationFactory()
    cal = factory.createOption(op)
    cal.op1 = int(opa)
    cal.op2 = int(opb)
    print(cal.GetResult())



class LeiFeng:
    def Sweep(self):
        print( "LeiFeng sweep")

class Student(LeiFeng):
    def Sweep(self):
        print("Student sweep")

class Volenter(LeiFeng):
    def Sweep(self):
        print("Volenter sweep")

class LeiFengFactory:
    def CreateLeiFeng(self):
        temp = LeiFeng()
        return temp

class StudentFactory(LeiFengFactory):
    def CreateLeiFeng(self):
        temp = Student()
        return temp

class VolenterFactory(LeiFengFactory):
    def CreateLeiFeng(self):
        temp = Volenter()
        return temp

if __name__ == "__main__":
    sf = StudentFactory()
    s=sf.CreateLeiFeng()
    s.Sweep()
    sdf = VolenterFactory()
    sd=sdf.CreateLeiFeng()
    sd.Sweep()


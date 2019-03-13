class Target:
    def Request(self):
        print("common request.")

class Adaptee(Target):
    def SpecificRequest(self):
        print("specific request.")

class Adapter(Target):
    def __init__(self, ada):
        self.adaptee = ada
    def Request(self):
        self.adaptee.SpecificRequest()

if __name__ == "__main__":
    adaptee = Adaptee()
    adapter = Adapter(adaptee)
    adapter.Request()
#remote procedure call 简称rpc 远程过程调用
#python中有baseManager 包可以实现远程调用
from twisted.web import xmlrpc, server

class Test(xmlrpc.XMLRPC):
    def xmlrpc_add(self, a, b):
        return a+b

    def xmlrpc_fault(self):
        raise xmlrpc.Fault(123, "the fault procedure is faulty")

if __name__ == '__main__':
    from twisted.internet import reactor
    r = Test()
    reactor.listemTCP(7080, server.Site(r))
    reactor.run()




#client code is simple
import xmlrpclib
s = xmlrpclib.Server('http://localhost:7080')
print(s.add(3,4))





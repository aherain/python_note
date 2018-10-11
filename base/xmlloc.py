from xmlrpc.client import ServerProxy
if __name__ == '__main__':
    s = ServerProxy('http://localhost:8000')
    print(s.pow(3, 5))
    print(s.add(3, 9))
    print(s.div(7, 3))



#python3 中的模块 xmlrpc  可以实现调用远程的服务端python程序
#xmlrpc.sever 实现服务端程序的绑定
#xmlrpc.client 启动客户端程序调用指定在远程服务端的程序

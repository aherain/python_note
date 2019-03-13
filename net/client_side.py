import socket

#address
HOST = '127.0.0.1'
PORT = 8000

request = b'can you hear me ?'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

#send message
s.sendall(request)

#receive message
reply = s.recv(1024)

print('reply is : %s' % reply)

s.close()

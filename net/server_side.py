# server side

import socket

#Address
HOST = '127.0.0.1'
PORT = 8000

reply = b'Yes'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

s.listen(3)

conn, addr = s.accept()

request = conn.recv(1024)

print("request is", request)
print("connected by", addr)

conn.sendall(reply)

#close connection
conn.close()


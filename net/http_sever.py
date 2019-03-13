import socket

HOST = '127.0.0.1'
PORT = 8000

#prepare HTTP response

text_content =b''''
HTTP/1.x 200 OK
Content-Type: text/html

<htm>
<head>
<title>WOW</title>
</head>
<body>
<p>Wow, this is python server</p>
<img src="11.png"/>
</body>
</html>
'''

#read picture, put into HTTP format
f = open('11.png', 'rb')
pic_content = '''
HTTP/1.x 200 OK
Content-type: image/png

'''

pic_content = pic_content.encode('utf-8') + f.read()

f.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

while True:
    s.listen(3)
    conn, addr = s.accept()
    request = conn.recv(1024)
    request = request.decode("utf-8")
    method = request.split(' ')[0]
    src = request.split(' ')[1]
    print(method, src)

    if method == "GET":
        if src == '/11.png':
            content = pic_content
        else:
            content = text_content
        conn.sendall(content)
    conn.close()
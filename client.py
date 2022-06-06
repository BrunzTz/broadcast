import socket

IP_SERVIDOR = "127.0.0.1"
PORTA_SERVIDOR = 4200

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((IP_SERVIDOR, PORTA_SERVIDOR))
msg = b"Hello Ettore"
print(f"Request: {msg.decode('utf-8')}")
s.sendall(msg)
dados = s.recv(1024)
print(f"Response: {dados.decode('utf-8')}")
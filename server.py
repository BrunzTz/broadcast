from ast import arg
import socket
import threading

def atenderCliente(cliente, endereco):
    print(f"conexao ao cliente {endereco}")
    while True:
        dadosRecebidos = cliente.recv(1024)
        if not dadosRecebidos:
            break
    mensagem = dadosRecebidos.decode('utf-8')
    print(f"O cliente {endereco} enviou: {mensagem}")

MEU_IP = "127.0.0.1"
PORTA = 4200
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((MEU_IP, PORTA))
s.listen(20)
print("Aguardando por conexões...")
print(f"meu ip: {MEU_IP} e porta: {PORTA}")

while True:
    cliente, endereco = s.accept()
    print(f"Conexão realizada com o cliente {endereco}")
    threading.Thread(target=atenderCliente, arg=(cliente, endereco))
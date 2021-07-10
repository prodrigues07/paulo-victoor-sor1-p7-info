import threading
import socket

host = '127.0.0.1'
port = 5555
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clientes = []
apelidos = []

def broadcast(message):
    for client in clientes:
        client.send(message)

def handle_msg(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            i = clientes.index(client)
            clientes.remove(client)
            apelido = apelidos[i]
            client.close()
            broadcast(f'{apelido} deixou a conversa!'.encode('utf-8'))
            print(f'{apelido} deixou a conversa!')
            apelidos.remove(apelido)
            break

def receive_client():
    while True:
        client, address = server.accept()
        print(f'Conexão estabelecida com {str(address)}')

        client.send('NICK'.encode('utf-8'))
        apelido = client.recv(1024).decode('utf-8')
        apelidos.append(apelido)
        clientes.append(client)

        print(f'O apelido do cliente é {apelido}!')
        broadcast(f'{apelido} se juntou à conversa!'.encode('utf-8'))
        #client.send('Conectado ao servidor!'.encode('utf-8'))

        chat = threading.Thread(target=handle_msg, args=(client,))
        chat.start()

print('Servidor aberto...')
receive_client()
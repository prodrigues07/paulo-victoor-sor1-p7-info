import threading
import socket

apelido = input('Escolha seu apelido: ')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5555))

def receive_client():
    while True:
        try:
            data = client.recv(1024).decode('utf-8')
            if data == 'NICK':
                client.send(apelido.encode('utf-8'))
            else:
                print(data)
        except:
            print('Um erro ocorreu. Tente novamente!')
            client.close()
            break

def write_msg():
    while True:
        data = f'{apelido}: {input("")}'
        client.send(data.encode('utf-8'))

receive_thread = threading.Thread(target=receive_client)
receive_thread.start()
write_thread = threading.Thread(target=write_msg)
write_thread.start()
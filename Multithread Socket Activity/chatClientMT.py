import sys
import socket
import threading
import tincanchat

nickname = input('Choose a nickname: ')

HOST = sys.argv[-1] if len(sys.argv) > 1 else '127.0.0.1'
PORT = tincanchat.PORT

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print('An error occured!')
            client.close()
            break

receive_thread = threading.Thread(target=receive)
receive_thread.start()

def handle_input(sock):
    print("Type messages, enter to send. 'q' to quit")
    while True:
        msg = input()  # Blocks
        if msg == 'q':
            sock.shutdown(socket.SHUT_RDWR)
            sock.close()
            break
        try:
            tincanchat.send_msg(sock, msg)  # Blocks until sent
        except (BrokenPipeError, ConnectionError):
            sys.stdout.flush()
            break

if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    print('Connected to {}:{}'.format(HOST, PORT))

    thread = threading.Thread(target=handle_input,
                              args=[sock],
                              daemon=True)
    thread.start()
    rest = bytes()
    addr = sock.getsockname()
    while True:
        try:
            (msgs, rest) = tincanchat.recv_msgs(sock, rest)
            for msg in msgs:
                print(msg)
        except ConnectionError:
            print('Connection to server closed')
            sock.close()
            break

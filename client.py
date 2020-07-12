import socket
import os

os.system('cls')

with socket.socket() as client_socket:

    client_socket.connect(('localhost', 12345))

    msg = ''

    while msg != 'quit':
        msg = client_socket.recv(1024).decode('utf-8')
        print(msg)
        print(' '*30, 'Enter Message:', end='')
        msg = input()
        client_socket.send(bytes(msg, 'utf-8'))

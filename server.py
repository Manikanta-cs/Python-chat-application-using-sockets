import socket
import os

os.system('cls')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:

    server_socket.bind(('localhost', 12345))

    server_socket.listen(5)

    while True:
        cli, addr = server_socket.accept()

        with cli:
            cli.send(b"Now You are connected\nsend `quit` to quit the connection.")

            msg = ''
            while msg != 'quit':
                msg = cli.recv(1024)
                print(msg.decode('utf-8'))
                print(' '*30, 'Enter Message:', end='')
                msg = input()
                cli.send(bytes(msg, 'utf-8'))

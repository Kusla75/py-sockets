import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 420

server_socket.bind((host, port))

server_socket.listen(5)

while True:
    client_socket, address = server_socket.accept()

    print('Server succesfully connected to ' + str(address))
    message = 'Welcome to server!'

    client_socket.send(message.encode('utf-8'))
    client_socket.close()

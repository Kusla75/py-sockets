import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 420
server_socket.bind((host, port))
server_socket.listen(3)
socket_list = []
names_list = [] 
messages_history = []

client_socket, address = server_socket.accept()
name = client_socket.recv(1024).decode('utf-8')
names_list.append(name)
socket_list.append(client_socket)
print(f'Connection established with {name} with IP address {address[0]}')

client_socket, address = server_socket.accept()
name = client_socket.recv(1024).decode('utf-8')
names_list.append(name)
socket_list.append(client_socket)
print(f'Connection established with {name} with IP address {address[0]}')

while True:
    message = socket_list[0].recv(1024)
    if message:
        socket_list[1].send(message)
        print(f'Message sent from {names_list[0]} to {names_list[1]}')
        messages_history.append(message.decode('utf-8'))

    message = socket_list[1].recv(1024)
    if message:
        socket_list[0].send(message)
        print(f'Message sent from {names_list[1]} to {names_list[0]}')
        messages_history.append(message.decode('utf-8'))
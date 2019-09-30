import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_ip = '192.168.56.1'
port = 420

client_socket.connect((server_ip, port))

server_message = client_socket.recv(1024)

client_socket.close()

print(server_message.decode('utf-8'))
import socket

# create client socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_ip = '192.168.56.1'
port = 420

# connect client socket to server using servers ip and port
client_socket.connect((server_ip, port))

# recieve message from server
server_message = client_socket.recv(1024)

client_socket.close()

# decode and print recieved message
print(server_message.decode('utf-8'))
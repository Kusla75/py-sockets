import socket
import platform
import os

def write_messages(messages_history):
    for message in messages_history:
        print(message)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host_name = socket.gethostname()
server_ip = '192.168.56.1'
port = 420
messages_history = []
promt = host_name + ': '

client_socket.connect((server_ip, port))
client_socket.send(host_name.encode('utf-8'))

while True:
    if platform.system() == "Windows":
        os.system('cls')
    elif platform.system() == "Linux":
        os.system('clear')
    else:
        pass

    write_messages(messages_history)

    message = input(promt)
    message =  promt + message 
    client_socket.send(message.encode('utf-8'))
    messages_history.append(message)

    new_message = client_socket.recv(1024)
    new_message = new_message.decode('utf-8')
    messages_history.append(new_message)

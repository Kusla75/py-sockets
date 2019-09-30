import socket

# create server socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get name of host machine
host = socket.gethostname()
port = 420

# bind host name and port to socket object
server_socket.bind((host, port))

# wait for new connections
server_socket.listen(5)

while True:
    # accept new established connection
    # returns socket object and (soc ip address, soc port)
    client_socket, address = server_socket.accept()

    print('Server succesfully connected to ' + str(address))
    message = 'Welcome to server!'

    # decode and send message to client socket
    client_socket.send(message.encode('utf-8'))
    client_socket.close()

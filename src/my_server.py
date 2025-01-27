import socket

server_socket = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))
server_socket.listen(1)
print ('Server is waiting binding')

data = ''
while True:
    client_socket, client_address = server_socket.accept ()
    print (f'Link is exited {client_address}')

    data = client_socket.recv(1024)
    if data.decode() == 'stop':
        break
    print (f'Data is receive {data.decode()}')

    client_socket.sendall(b'Hello client !')

client_socket.close()


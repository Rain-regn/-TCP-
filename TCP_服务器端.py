import socket as s

socket_obj = s.socket(s.AF_INET, s.SOCK_STREAM)
socket_obj.bind(('0.0.0.0', 8080))
socket_obj.listen(5)
print('-'*10,'>loading<','-'*10,sep='')

client_socket, client_address = socket_obj.accept()
print('C -->>', client_socket)

info = client_socket.recv(1024).decode('utf-8')
while info!='quit':
    if info!='':
        print('C >>',info)

    data = input('S >>')
    client_socket.send(data.encode('utf-8'))

    if data=='quit':
        break

    info = client_socket.recv(1024).decode('utf-8')

client_socket.close()
socket_obj.close()
import socket as s

client_socket = s.socket()
client_socket.connect(('16.tcp.cpolar.top',10632))
print('-'*10,'>loading<','-'*10,sep='')

info = ''
while info!='quit':
    send_data = input('C >>')
    client_socket.send(send_data.encode('utf-8'))

    if send_data=='quit':
        break

    info = client_socket.recv(1024).decode('utf-8')
    print('S >>',info)

client_socket.close()
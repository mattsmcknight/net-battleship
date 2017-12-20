import socket



def open_host():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('0.0.0.0', 8675)
    sock.bind(server_address)
    sock.listen(10)
    return sock

def accept_client(sock2):
    sock = sock2.accept()[0]
    return sock

def open_client(host = 'localhost'):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ((host, 8675))
    sock.connect(server_address)
    return sock

def send_first_turn(sock, myturn):
    sock.send(bytes('{}\r'.format(myturn), 'utf8'))

def receive_first_turn(sock):
    a = ' '
    b = ''
    while a != '\r':
        a = sock.recv(1).decode("utf8")
        b = b + a
    return b == 'True'

def send_order(sock, row, column, success = 'First_Turn'):
    message = '{},{},{}\r'.format(row, column, str(success))
    sock.send(bytes(message, 'utf8'))

def recieve_order(sock):
    a = ' '
    b = ''
    while a != '\r':
        a = sock.recv(1).decode("utf8")
        b = b + str(a)
    b = b.split(',')
    b[2] = b[2] == 'True'
    return (int(b[0]), b[1]), b[2]

def close_connection(sock):
    sock.close()

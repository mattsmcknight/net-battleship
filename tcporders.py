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
    sock.settimeout(5)
    try:
        sock.send(bytes('{}\r'.format(myturn), 'utf8'))
    except:
        pass

def receive_first_turn(sock):
    b = ''
    while True:
        a = sock.recv(1).decode("utf8")
        if a == '\r':
            break
        b = b + str(a)
    return b == 'True'

def send_ack(sock):
    sock.send(bytes('ack\r'), 'utf8')

def receive_ack(sock):
    b = ''
    while True:
        sock.settimeout(5)
        try:
            a = sock.recv(1).decode("utf8")
        except:
            a = '\r'
        if a == '\r':
            break
        b = b + str(a)
    return b == 'ack'


def send_order(sock, row, column, success = 'First_Turn'):
    message = '{},{},{}\r'.format(row, column, str(success))
    sock.send(bytes(message, 'utf8'))

def receive_order(sock):
    b = ''
    while True:
        a = sock.recv(1).decode("utf8")
        if a == '\r':
            break
        b = b + str(a)
    return b

def send_winner(sock):
    message = 'Winner!\r'
    sock.send(bytes(message, 'utf8'))

def close_connection(sock):
    sock.close()

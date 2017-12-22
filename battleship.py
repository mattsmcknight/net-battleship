import sys, time, os, random

from boards import Board
from places import place_pieces
from tcporders import *

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def initialize():
    player = Board()
    player.playerboard()
    opponent = Board()
    return player, opponent


def connect(server, client = 'None'):
    if server == 'host':
        sock2 = open_host()
        print('Waiting for other Player...')
        sock = accept_client(sock2)
        print('Player 2 connected.')

    if server == 'client':
        sock2 = None
        print('Connecting to host...')
        sock = open_client(client)
        print ('Connection Established.')
    return sock2, sock


def split_order(b):
    b = b.split(',')
    b[2] = b[2] == 'True'
    return (b[0], b[1]), b[2]


def take_order(opponent_board, player_board):
    print(opponent_board)
    print(player_board)

def init_pieces()
    carrier = Piece('c', 5, 'carrier')
    battleship1, battleship2 = Piece('b', 4, 'battleship'), Piece('b', 4, 'battleship')
    cruiser1, cruiser2, cruiser3 = Piece('u', 3, 'cruiser'), Piece('u', 3, 'cruiser'), Piece('u', 3, 'cruiser')
    submarine1, submarine2, submarine3 = Piece('s', 3, 'submarine'), Piece('s', 3, 'submarine'), Piece('s', 3, 'submarine')
    destroyer1, destroyer2 = Piece('d', 2, 'destroyer'), Piece('d', 2, 'destroyer')
    ships = [carrier]#battleship1, battleship2, cruiser1, cruiser2, cruiser3, submarine1, submarine2, submarine3,
             destroyer1, destroyer2]
    return ships


if __name__ == '__main__':
    server = sys.argv[1]
    try:
        client = sys.argv[2]
    except:
        client = None

    player_board, opponent_board, = initialize()
    ships = init_pieces()
    place_pieces(player_board, ships)
    sock2, sock = connect(server, client)

    if server == 'host':
        turn = random.randint(0,1)
        time.sleep(2)
        send_first_turn(sock, str(turn == 0))
        print(turn)
        if turn == 0:
            receive_order(sock)

    if server == client:
        turn == receive_first_turn(sock)
        print(turn)
        if not turn:
            receive_order

    time.sleep(10)
    # Turn Loop

    # Win condition tests if all pieces in piece list add to 0
    # Win condition tests if received 'Winner!'
    # Win condition sets winner = True or False

    # Turn Loop broken by win conditions.

    # Sync boards by hitting all squares

    close_connection(sock)

    print(opponent_board)
    print(player_board)
    if winner:
        print('You have Won!')
    else:
        print('You have Lost!')










import sys, time, os

from boards import Board
from pieces import Piece
from tcporders import *

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def initialize(server, client = None):
    player = Board()
    player.playerboard()
    opponent = Board()
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

    return player, opponent, sock2, sock


def split_order(b):
    b = b.split(',')
    b[2] = b[2] == 'True'
    return (b[0], b[1]), b[2]


def place_pieces():
    carrier = Piece('c', 5, 'carrier')
    battleship1, battleship2 = Piece('b', 4, 'battleship'), Piece('b', 4, 'battleship')
    cruiser1, cruiser2, cruiser3 = Piece('u', 4, 'cruiser'), Piece('u', 4, 'cruiser'), Piece('u', 4, 'cruiser')
    submarine1, submarine2, submarine3 = Piece('s', 4, 'submarine'), Piece('s', 4, 'submarine'), Piece('s', 4, 'submarine')
    destroyer1, destroyer2 = Piece('d', 4, 'destroyer'), Piece('d', 4, 'destroyer')
    ships = [carrier, battleship1, battleship2, cruiser1, cruiser2, cruiser3, submarine1, submarine2, submarine3,
             destroyer1, destroyer2]
    for ship in ships:
        cls()
        print(player_board)
        print('Place your {}:'.format(ship))
        print('row: [1-10]')
        for _ in range(2):
            row = input()
            try:
                row = int(row)
                if row > 0 and row < 11:
                    break
                else:
                    raise ValueError('Number out of range')
            except Exception as excpt:
                print(excpt)
                print('Try Again)')
        print('column: [a-j]')
        for _ in range(3):
            column = input()
            try:
                column = column.lower()
                print(column)
                print(len(column))
                if column in 'a b c d e f g h i j' and len(column) == 1:
                    break
                else:
                    raise ValueError('Column out of range')
            except Exception as excpt:
                print(excpt)
                print('Try Again')
        else:
            close_connection(sock)
            quit()
        print('(H)orizontal or (V)ertical: [hv]')
        for _ in range(2):
            orient = input()
            try:
                orient = orient.lower()
                if orient in 'h v' and len(column) == 1:
                    break
                else:
                    raise ValueError('Column out of range')
            except Exception as excpt:
                print(excpt)
                print('Try Again')
        else:
            close_connection(sock)
            quit()

        if orient == 'h':
            if (ord(column) + ship.length) > 10:
                column = chr(ord(column) - (ord(column) + ship.length - 10))
            ship.place_horizontal(player_board, row, column)
        if orient == 'v':
            if (row + ship.length) > 10:
                row = row - (row + ship.length - 10)
            ship.place_vertical(player_board, row, column)
    cls()
    print(player_board)
    return ships

if __name__ == '__main__':
    server = sys.argv[1]
    try:
        client = sys.argv[2]
    except:
        client = None

    player_board, opponent_board = Board(), Board()
    player_board.playerboard()

    # player_board, opponent_board, sock2, sock = initialize(server, client)

    ships = place_pieces()

    # Check host or client
    # If host, Roll for first Turn If client, wait for winner

    # Winner takes the first turn outside of the Turn Loop

    # Turn Loop starts with loser.

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










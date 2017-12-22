import sys, time, os, random

from boards import Board
from pieces import Piece
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


def take_order(opponent_board, player_board, sock):
    cls()
    print(opponent_board)
    print(player_board)
    print('Your move.')
    for _ in range(3):
        print('row: [1-10]')
        for _ in range(3):
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
        else:
            sock.close()
            quit()
        print('column: [a-j]')
        for _ in range(3):
            column = input()
            try:
                column = column.lower()
                if column in 'a b c d e f g h i j' and len(column) == 1:
                    break
                else:
                    raise ValueError('Column out of range')
            except Exception as excpt:
                print(excpt)
                print('Try Again')
        else:
            sock.close()
            quit()
        return (row, column)
def init_pieces():
    carrier = Piece('c', 5, 'carrier')
    battleship1, battleship2 = Piece('b', 4, 'battleship'), Piece('b', 4, 'battleship')
    cruiser1, cruiser2, cruiser3 = Piece('u', 3, 'cruiser'), Piece('u', 3, 'cruiser'), Piece('u', 3, 'cruiser')
    submarine1, submarine2, submarine3 = Piece('s', 3, 'submarine'), Piece('s', 3, 'submarine'), Piece('s', 3, 'submarine')
    destroyer1, destroyer2 = Piece('d', 2, 'destroyer'), Piece('d', 2, 'destroyer')
    ships = [carrier]#battleship1, battleship2, cruiser1, cruiser2, cruiser3, submarine1, submarine2, submarine3,
             # destroyer1, destroyer2]
    return ships


if __name__ == '__main__':
    server = sys.argv[1]
    try:
        client = sys.argv[2]
    except:
        client = None

    player_board, opponent_board, = initialize()
    sock2, sock = connect(server, client)
    ships = init_pieces()
    place_pieces(player_board, ships, sock)

    if server == 'host':
        turn = random.randint(0,1)
        while True:
            send_first_turn(sock, str(turn == 0))
            if receive_ack(sock):
                break
        sock.settimeout(100000)
        if turn == 0:
            time.sleep(1)
            print('waiting for other player...')
            your_turn, result = split_order(receive_order(sock))
            my_result = player_board.hit(*your_turn)
            for ship in ships:
                ship.remove_life(*your_turn)
        else:
            my_result = False

    if server == 'client':
        turn = receive_first_turn(sock)
        time.sleep(5)
        send_ack(sock)
        if not turn:
            print('waiting for other player...')
            your_turn, result = split_order(receive_order(sock))
            my_result = player_board.hit(*your_turn)
            for ship in ships:
                ship.remove_life(*your_turn)
        else:
            my_result = False

    while True:
        row, column = take_order(opponent_board, player_board, sock)
        time.sleep(2)
        send_order(sock, row, column, my_result)
        your_turn, result = split_order(receive_order(sock))
        if result == 'Winner!':
            winner = True
            break
        my_result = player_board.hit(*your_turn)
        opponent_board.hit(row, column, result)
        for ship in ships:
            ship.remove_life(*your_turn)
        if sum(ships) == 0:
            time.sleep(2)
            send_winner(sock)
            winner = False
            break



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










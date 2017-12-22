import sys, time, os

from boards import Board
from places import place_pieces
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


if __name__ == '__main__':
    server = sys.argv[1]
    try:
        client = sys.argv[2]
    except:
        client = None

    player_board, opponent_board = Board(), Board()
    player_board.playerboard()

    # player_board, opponent_board, sock2, sock = initialize(server, client)

    ships = place_pieces(player_board)

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










import sys, time

from boards import Board
from pieces import Piece
from tcporders import *


def initialize():
    player = Board()
    player.playerboard()
    opponent = Board()
    return player, opponent


# place pieces on table

# make move logic

# test hit or miss

# test win condition

# create network host or client sockets

# send commands over network


if __name__ == '__main__':
    player_board, opponent_board = initialize()

    server = sys.argv[1]
    client = sys.argv[2]
    carrier = Piece('c', 5)
    carrier.place_vertical(player_board, 1, 'c')
    print(player_board)
    print(opponent_board)
    print((str(True)))

    if server == 'host':
        sock2 = open_host()
        print('socket opened')
        sock = accept_client(sock2)
        print('socket accepted')
        time.sleep(5)
        send_first_turn(sock, 'True')
        print('first turn sent')
        time.sleep(2)
        send_order(sock, 3, 'c')
        print('first order sent')
        your_turn, result = recieve_order(sock)
        print('first received order')
        opponent_board.opponenthit(3, 'c', result)
        my_result = player_board.hit(*your_turn)
        time.sleep(2)
        send_order(sock, 3, 'd', my_result)
        print('second order sent')
        your_turn, result = recieve_order(sock)
        print('second received order')
        opponent_board.opponenthit(3, 'c', result)
        my_result = player_board.hit(*your_turn)

    if server == 'client':
        sock = open_client(client)
        print ('socket opened')
        whose_turn = receive_first_turn(sock)
        print('first turn received')
        if whose_turn:
            print(str(whose_turn))
        your_turn, result = recieve_order(sock)
        print('first received order')
        my_result = player_board.hit(*your_turn)
        print(my_result)
        time.sleep(2)
        send_order(sock, 2, 'c', my_result)
        print('first order sent')
        your_turn, result = recieve_order(sock)
        print('second received order')
        my_result = player_board.hit(*your_turn)
        opponent_board.opponenthit(2, 'c', result)
        time.sleep(2)
        send_order(sock, 2, 'd', my_result)
        print('second order sent')

    close_connection(sock)
    print(player_board)
    print(opponent_board)









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

    if server == 'host':
        sock2 = open_host()
        sock = accept_client(sock2)
        time.sleep(5)
        send_first_turn(sock, 'True')

        time.sleep(2)
        send_order(sock, 3, 'c')

        your_turn, result = recieve_order(sock)
        opponent_board.opponenthit(3, 'c', result)
        my_result = player_board.hit(*your_turn)

        time.sleep(2)
        send_order(sock, 3, 'd', my_result)

        your_turn, result = recieve_order(sock)
        opponent_board.opponenthit(3, 'd', result)
        my_result = player_board.hit(*your_turn)

        time.sleep(2)
        send_order(sock, 3, 'd', my_result)

    if server == 'client':
        sock = open_client(client)
        whose_turn = receive_first_turn(sock)
        your_turn, result = recieve_order(sock)
        my_result = player_board.hit(*your_turn)

        time.sleep(2)
        send_order(sock, 2, 'c', my_result)

        your_turn, result = recieve_order(sock)
        my_result = player_board.hit(*your_turn)
        opponent_board.opponenthit(2, 'c', result)

        time.sleep(2)
        send_order(sock, 2, 'd', my_result)

        your_turn, result = recieve_order(sock)
        my_result = player_board.hit(*your_turn)
        opponent_board.opponenthit(2, 'd', result)

    close_connection(sock)

    print(opponent_board)
    print(player_board)








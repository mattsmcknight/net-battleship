from boards import Board
from pieces import Piece


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

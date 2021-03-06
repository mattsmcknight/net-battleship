import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def place_pieces(player_board, ships, sock):
    for ship in ships:
        cls()
        print(player_board)
        print('Place your {}:'.format(ship))
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
                sock.close
                quit()

            if orient == 'h':
                print('{} {} {}'.format(ord(column), ship.length, ord(column) + ship.length))
                if (ord(column) + ship.length) > 106:
                    column = chr(ord(column) - (ord(column) + ship.length - 10) + 97)
                if ship.place_horizontal(player_board, row, column):
                    break
                else:
                    print('Occupied, try again.')

            if orient == 'v':
                if (row + ship.length) > 10:
                    row = row - (row + ship.length - 10) + 1
                if ship.place_vertical(player_board, row, column):
                    break
                else:
                    print('Occupied, try again.')
        else:
            sock.close()
            quit()
    cls()
    print(player_board)
    return ships
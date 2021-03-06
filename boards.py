import collections

class Board:
    def __init__(self):
        boardlist = []
        boardtmp = collections.OrderedDict()
        filled = '~'
        letters = "abcdefghij"
        for row in range(1, 11):
            for column in letters:
                boardtmp[column] = filled
            boardlist.append(boardtmp.copy())
            boardtmp.clear()
        self.board = boardlist

    def __iter__(self):
        for item in self.boardlist:
            yield item


    def __str__(self):
        lines = "    a  b  c  d  e  f  g  h  i  j "
        for count, row in enumerate(self.board):
            if count == 9:
                lines = lines + "\n{} ".format(count + 1)
            else:
                lines = lines + "\n{}  ".format(count + 1)
            for column in row.values():
                lines = lines + " {} ".format(column)
        return(lines)

    def __getitem__(self, item):
        return self.board[item]

    def fillboard(self, row, column, value):
        row = row - 1
        self.board[row][column] = value
        return self.board


    def playerboard(self):
        for row in self.board:
            for key in row.keys():
                row[key] = '~'

    def check_occupied(self, row, column):
        row = row - 1
        print('{}, {}'.format(row, column))
        if self.board[row][column] != '~':
            return True
        return False

    def hit(self, row, column):
        row = row - 1
        if self.board[row][column] == '~':
            self.board[row][column] = 'O'
            return False
        else:
            self.board[row][column] = 'X'
            return True
        return False

    def opponenthit(self, row, column, success):
        row = row - 1
        if success:
            self.board[row][column] = 'X'
            return True
        else:
            self.board[row][column] = 'O'
            return False

class Piece:
    def __init__(self, piecetype, length):
        self.piecetype = piecetype
        self.length = length

    def place_horizontal(self, board,  row, column):
        for x in range(self.length):
            if board.check_occupied(row, chr(ord(column) + x)):
                return False
        for x in range(self.length):
            board.fillboard(row, chr(ord(column) + x), self.piecetype)
        return True

    def place_vertical(self, board,  row, column):
        for x in range(self.length):
            if board.check_occupied(row + x, column):
                return False
        for x in range(self.length):
            board.fillboard(row + x, column, self.piecetype)
        return True

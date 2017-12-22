class Piece:
    def __init__(self, piecetype, length, name):
        self.piecetype = piecetype
        self.length = length
        self.lives = length
        self.location = []
        self.name = name

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
            self.location.append((row + x, column))
        return True

    def remove_life(self, row, column):
        if (row, column) in self.location:
            self.lives -= 1
        return self.lives

    def __repr__(self):
        return int(self.lives)

    def __add__(self, other):
        return int(self.lives) + other

    def __radd__(self, other):
        return self + other

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

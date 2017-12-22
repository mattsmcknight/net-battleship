import unittest
from battleship import *

class BattleShipTestCase(unittest.TestCase):
    def setUp(self):
        self.player_board, self.opponent_board = initialize()

    def test_player_boards(self):
        testboard = """    a  b  c  d  e  f  g  h  i  j 
1   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~ 
2   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~ 
3   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~ 
4   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~ 
5   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~ 
6   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~ 
7   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~ 
8   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~ 
9   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~ 
10  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~ """
        self.assertEqual('{}'.format(self.player_board), testboard, 'Does not match')

    def test_opponent_boards(self):
        testboard = """    a  b  c  d  e  f  g  h  i  j 
1   ?  ?  ?  ?  ?  ?  ?  ?  ?  ? 
2   ?  ?  ?  ?  ?  ?  ?  ?  ?  ? 
3   ?  ?  ?  ?  ?  ?  ?  ?  ?  ? 
4   ?  ?  ?  ?  ?  ?  ?  ?  ?  ? 
5   ?  ?  ?  ?  ?  ?  ?  ?  ?  ? 
6   ?  ?  ?  ?  ?  ?  ?  ?  ?  ? 
7   ?  ?  ?  ?  ?  ?  ?  ?  ?  ? 
8   ?  ?  ?  ?  ?  ?  ?  ?  ?  ? 
9   ?  ?  ?  ?  ?  ?  ?  ?  ?  ? 
10  ?  ?  ?  ?  ?  ?  ?  ?  ?  ? """
        self.assertEqual('{}'.format(self.opponent_board), testboard, 'Does not match')


    def test_piece(self):
        carrier = Piece('c', 5)
        c_test_true = carrier.place_vertical(self.player_board, 1, 'c')
        c_test_false = carrier.place_horizontal(self.player_board, 2, 'a')
        self.assertEqual(c_test_true, True, 'Carrier not placed')
        self.assertEqual(c_test_false, False, 'Carrier placed overlapped')
        testboard = """    a  b  c  d  e  f  g  h  i  j 
1   ~  ~  c  ~  ~  ~  ~  ~  ~  ~ 
2   ~  ~  c  ~  ~  ~  ~  ~  ~  ~ 
3   ~  ~  c  ~  ~  ~  ~  ~  ~  ~ 
4   ~  ~  c  ~  ~  ~  ~  ~  ~  ~ 
5   ~  ~  c  ~  ~  ~  ~  ~  ~  ~ 
6   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~ 
7   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~ 
8   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~ 
9   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~ 
10  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~ """
        self.assertEqual('{}'.format(self.player_board), testboard, 'Does not match')


    def testhit(self):
        carrier = Piece('c', 5)
        carrier.place_vertical(self.player_board, 1, 'c')
        self.assertEqual(self.player_board.hit(3, 'c'), True, 'Hit not detected')
        self.assertEqual(self.player_board.hit(3, 'd'), False, 'Hit detected in error')
        self.assertEqual(carrier.remove_life(3, 'c'), 4, 'Wrong Lives Left')
        testboard = """    a  b  c  d  e  f  g  h  i  j 
1   ~  ~  c  ~  ~  ~  ~  ~  ~  ~ 
2   ~  ~  c  ~  ~  ~  ~  ~  ~  ~ 
3   ~  ~  X  ~  ~  ~  ~  ~  ~  ~ 
4   ~  ~  c  ~  ~  ~  ~  ~  ~  ~ 
5   ~  ~  c  ~  ~  ~  ~  ~  ~  ~ 
6   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~ 
7   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~ 
8   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~ 
9   ~  ~  ~  ~  ~  ~  ~  ~  ~  ~ 
10  ~  ~  ~  ~  ~  ~  ~  ~  ~  ~ """
        self.assertEqual('{}'.format(self.player_board), testboard, 'Does not match')

    def testopponenthit(self):
        self.assertEqual(self.opponent_board.opponenthit(3, 'c', True), True, 'Hit not detected')
        self.assertEqual(self.opponent_board.opponenthit(3, 'd', False), False, 'Hit detected in error')
        testboard = """    a  b  c  d  e  f  g  h  i  j 
1   ?  ?  ?  ?  ?  ?  ?  ?  ?  ? 
2   ?  ?  ?  ?  ?  ?  ?  ?  ?  ? 
3   ?  ?  X  ~  ?  ?  ?  ?  ?  ? 
4   ?  ?  ?  ?  ?  ?  ?  ?  ?  ? 
5   ?  ?  ?  ?  ?  ?  ?  ?  ?  ? 
6   ?  ?  ?  ?  ?  ?  ?  ?  ?  ? 
7   ?  ?  ?  ?  ?  ?  ?  ?  ?  ? 
8   ?  ?  ?  ?  ?  ?  ?  ?  ?  ? 
9   ?  ?  ?  ?  ?  ?  ?  ?  ?  ? 
10  ?  ?  ?  ?  ?  ?  ?  ?  ?  ? """
        self.assertEqual('{}'.format(self.opponent_board), testboard, 'Does not match')

unittest.main()


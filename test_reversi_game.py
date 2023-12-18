import unittest
from reversi_game import ReversiGame

class TestReversiGame(unittest.TestCase):

    def setUp(self):
        self.reversi_game = ReversiGame()

    def test_startgame(self):
        self.assertEqual(self.reversi_game.get_score('X'), 2)
        self.assertEqual(self.reversi_game.get_score('O'), 2)
        self.assertEqual(self.reversi_game.current_player, 'X')
        self.assertFalse(self.reversi_game.is_game_over())

    def test_make_valid_move(self):
        self.assertTrue(self.reversi_game.is_valid_move(2, 3))
        self.reversi_game.make_move(2, 3)
        self.assertEqual(self.reversi_game.board[2][3], 'X')
        self.assertEqual(self.reversi_game.get_score('X'), 4)
        self.assertEqual(self.reversi_game.get_score('O'), 1)
        self.assertEqual(self.reversi_game.current_player, 'O')
        self.assertFalse(self.reversi_game.is_game_over())

    def test_get_winner(self):
        self.reversi_game.make_move(2, 3)  # Make a move to change the scores
        self.reversi_game.make_move(3, 2)
        self.reversi_game.make_move(4, 5)
        self.assertEqual(self.reversi_game.get_winner(), 'X')

if __name__ == '__main__':
    unittest.main()

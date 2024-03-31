# # test_tictactoe.py
#
# import unittest
# from ticTacToe import TicTacToe
#
# class TestTicTacToe(unittest.TestCase):
#     def test_initial_board(self):
#         game = TicTacToe()
#         expected_board = [
#             [' ', ' ', ' '],
#             [' ', ' ', ' '],
#             [' ', ' ', ' ']
#         ]
#         self.assertEqual(game.board, expected_board)
#
#     def test_make_move_valid(self):
#         game = TicTacToe()
#         self.assertTrue(game.make_move(0, 0))
#         self.assertEqual(game.board[0][0], 'X')
#
#     def test_make_move_invalid(self):
#         game = TicTacToe()
#         game.make_move(0, 0)
#         self.assertFalse(game.make_move(0, 0))  # Trying to make a move on an already occupied cell
#
#     def test_check_winner_row(self):
#         game = TicTacToe()
#         game.board = [
#             ['X', 'X', 'X'],
#             [' ', ' ', ' '],
#             [' ', ' ', ' ']
#         ]
#         self.assertEqual(game.check_winner(), 'X')
#
#     def test_check_winner_column(self):
#         game = TicTacToe()
#         game.board = [
#             ['X', ' ', ' '],
#             ['X', ' ', ' '],
#             ['X', ' ', ' ']
#         ]
#         self.assertEqual(game.check_winner(), 'X')
#
#     def test_check_winner_diagonal(self):
#         game = TicTacToe()
#         game.board = [
#             ['X', ' ', ' '],
#             [' ', 'X', ' '],
#             [' ', ' ', 'X']
#         ]
#         self.assertEqual(game.check_winner(), 'X')
#
#     def test_check_winner_no_winner(self):
#         game = TicTacToe()
#         game.board = [
#             ['X', 'O', 'X'],
#             ['X', 'O', 'O'],
#             ['O', 'X', 'X']
#         ]
#         self.assertIsNone(game.check_winner())
#
#     def test_is_board_full_false(self):
#         game = TicTacToe()
#         self.assertFalse(game.is_board_full())
#
#     def test_is_board_full_true(self):
#         game = TicTacToe()
#         game.board = [
#             ['X', 'O', 'X'],
#             ['X', 'O', 'O'],
#             ['O', 'X', 'X']
#         ]
#         self.assertTrue(game.is_board_full())
#
# if __name__ == '__main__':
#     unittest.main()

# 54912, 263


print(int('1011010',2))

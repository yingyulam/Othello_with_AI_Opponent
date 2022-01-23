'''
Yingyu Lin
CS 5001, Fall 2021
Final Project, Milestone 3

'''

import unittest
from board import Board
from computer_player import Computer_player
from handler import Handler

class Test_computer_player(unittest.TestCase):

    def test_computer_player_init(self):
        board = Board(8)
        computer = Computer_player(board)
        self.assertEqual(computer.name, "Computer player")
        self.assertEqual(computer.board, board)
        self.assertEqual(computer.board_size, 8)
        self.assertEqual(computer.move_checker.board, board)
        self.assertEqual(computer.terminal_board.board_size, 8)
        self.assertEqual(computer.tile.name, "Tile")

    def test_string_method(self):
        computer = Computer_player(Board(8))
        self.assertEqual(str(computer), "Computer Player for a 8 x 8 board")

    def test_equality(self):
        board1 = Board(8)
        board2 = Board(8)
        board3 = Board(4)
        computer1 = Computer_player(board1)
        computer2 = Computer_player(board2)
        computer3 = Computer_player(board3)
        self.assertEqual(computer1, computer2)
        self.assertNotEqual(computer1, computer3)

    def test_find_legal_moves(self):
        handler = Handler(8)
        handler.initiate_game()
        computer = Computer_player(handler.board)
        self.assertEqual(computer.find_legal_moves(), [(2, 4), (3, 5), (4, 2), (5, 3)])
        

    def test_get_vital_positions(self):
        computer = Computer_player(Board(8))
        expected = {'corners': [(0, 0), (0, 7), (7, 0), (7, 7)], \
            'edges': [(0, 1), (7, 1), (0, 2), (7, 2), (0, 3), (7, 3), (0, 4), \
                (7, 4), (0, 5), (7, 5), (0, 6), (7, 6), (1, 0), (1, 7), (2, 0),\
                     (2, 7), (3, 0), (3, 7), (4, 0), (4, 7), (5, 0), (5, 7), \
                         (6, 0), (6, 7), (7, 0), (7, 7)], \
                             'danger_zone': [(1, 1), (6, 1), (1, 2), (6, 2), \
                                 (1, 3), (6, 3), (1, 4), (6, 4), (1, 5), (6, 5),\
                                     (1, 6), (6, 6), (1, 1), (1, 6), (2, 1), \
                                         (2, 6), (3, 1), (3, 6), (4, 1), (4, 6),\
                                              (5, 1), (5, 6), (6, 1), (6, 6)]}
        self.assertEqual(computer.get_vital_positions(), expected)



def main():
    unittest.main(verbosity = 3)

if __name__ == "__main__":
    main()
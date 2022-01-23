'''
Yingyu Lin
CS 5001, Fall 2021
Final Project, Milestone 3

'''

import random
import unittest
from board import Board
from game_status import Game_status


class Test_game_status(unittest.TestCase):

    def test_game_status_init_basic(self):
        status = Game_status(Board(4))
        self.assertEqual(status.name, "Game_status")
        self.assertEqual(status.board, Board(4))
        self.assertEqual(status.board_size, 4)
        self.assertEqual(status.white_count, 0)
        self.assertEqual(status.black_count, 0)

    def test_game_status_init_error(self):
        with self.assertRaises(TypeError):
            status = Game_status("board")

    def test_printing(self):
        status = Game_status(Board(4))
        self.assertEqual(str(status), "Game status for a 4 x 4 board")

    def test_equality_true(self):
        status1 = Game_status(Board(4))
        status2 = Game_status(Board(4))
        self.assertEqual(status1, status2)
    
    def test_equality_false(self):
        status1 = Game_status(Board(4))
        status2 = Game_status(Board(8))
        self.assertNotEqual(status1, status2)
    
    def test_count_tiles_basic(self):
        board = Board(4)
        for row in range(board.get_board_size()):
            board.update(row, 0, "black")
            board.update(row, 2, "white")
        status = Game_status(board)
        self.assertEqual(status.count_tiles("black"), 4)
        self.assertEqual(status.count_tiles("white"), 4)

    def test_count_tiles_color_not_string(self):
        with self.assertRaises(TypeError):
            status = Game_status(Board(4))
            status.count_tiles(["black"])

    def test_count_tiles_color_not_valid(self):
        with self.assertRaises(ValueError):
            status = Game_status(Board(4))
            status.count_tiles("red")

    def test_get_tile_count(self):
        board = Board(4)
        for row in range(board.get_board_size()):
            board.update(row, 0, "black")
            board.update(row, 2, "white")
        board.update(2, 3, "black")
        status = Game_status(board)
        self.assertEqual(status.get_tile_count("black"), 5)
        self.assertEqual(status.get_tile_count("white"), 4)

    def test_get_tile_count_color_not_string(self):
        with self.assertRaises(TypeError):
            status = Game_status(Board(4))
            status.get_tile_count(["white"])

    def test_get_tile_count_color_not_valid(self):
        with self.assertRaises(ValueError):
            status = Game_status(Board(4))
            status.get_tile_count("red")

    def test_is_game_over_true_full_board(self):
        board = Board(8)
        for row in range(board.get_board_size()):
            for column in range(board.get_board_size()):
                board.update(row, column, random.choice(["white", "black"]))
        status = Game_status(board)
        self.assertTrue(status.is_gameover())  

    def test_is_game_over_no_legal_move_for_black(self):
        board = Board(8)
        for column in range(2):
            for row in range(board.get_board_size()):
                board.update(row, column, "white")
        for column in range(2,4):
            for row in range(board.get_board_size()):
                board.update(row, column, "black")
        status = Game_status(board)
        self.assertTrue(status.is_gameover())

    def test_is_game_over_no_legal_move_for_white(self):
        board = Board(8)
        for column in range(2):
            for row in range(board.get_board_size()):
                board.update(row, column, "black")
        for column in range(2,4):
            for row in range(board.get_board_size()):
                board.update(row, column, "white")
        board.update(0, 4, "white")
        status = Game_status(board)
        self.assertTrue(status.is_gameover())

    def test_check_winner_tie(self):
        board = Board(8)
        for column in range(4):
            for row in range(board.get_board_size()):
                board.update(row, column, "black")
        for column in range(4, board.get_board_size()):
            for row in range(board.get_board_size()):
                board.update(row, column, "white")
        status = Game_status(board)
        self.assertEqual(status.check_winner(), "tie")

    def test_check_winner_black(self):
        board = Board(8)
        for column in range(6):
            for row in range(board.get_board_size()):
                board.update(row, column, "black")
        for column in range(6, board.get_board_size()):
            for row in range(board.get_board_size()):
                board.update(row, column, "white")
        status = Game_status(board)
        self.assertEqual(status.check_winner(), "black")

    def test_check_winner_white(self):
        board = Board(8)
        for column in range(6):
            for row in range(board.get_board_size()):
                board.update(row, column, "white")
        for column in range(6, board.get_board_size()):
            for row in range(board.get_board_size()):
                board.update(row, column, "black")
        status = Game_status(board)
        self.assertEqual(status.check_winner(), "white")


    def test_get_winner_count(self):
        board = Board(8)
        for column in range(6):
            for row in range(board.get_board_size()):
                board.update(row, column, "white")
        for column in range(6, board.get_board_size()):
            for row in range(board.get_board_size()):
                board.update(row, column, "black")
        status = Game_status(board)
        self.assertEqual(status.get_winner_count(), 48)



def main():

    unittest.main(verbosity = 3)

if __name__ == "__main__":
    main()
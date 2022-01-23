'''
Yingyu Lin
CS 5001, Fall 2021
Final Project, Milestone 3

'''

import unittest
from handler import Handler
from board import Board
from terminal_tile import Terminal_tile
from terminal_board import Terminal_board
from converter import Converter
from move_checker import Move_checker
from computer_player import Computer_player


class Test_handler(unittest.TestCase):

    def test_handler_init(self):
        handler = Handler(8)
        self.assertEqual(handler.name, "Handler")
        self.assertEqual(handler.board, Board(8))
        self.assertEqual(handler.board.board_size, Board(8).board_size)
        self.assertEqual(handler.board_size, 8)
        self.assertEqual(handler.tile.name, "Tile")
        self.assertEqual(handler.terminal_board.name, "Terminal_board")
        self.assertEqual(handler.terminal_board.board_size, Terminal_board(8).board_size)
        self.assertEqual(handler.converter.name, "Converter")
        self.assertEqual(handler.converter.board_size, Converter(8).board_size)
        self.assertEqual(handler.move_checker.name, "Move_checker")
        self.assertEqual(handler.move_checker.board_size, Move_checker(handler.board).board_size)
        self.assertEqual(handler.computer_player.board_size, Computer_player(handler.board).board_size)
    
    def test_printing(self):
        handler = Handler(4)
        self.assertEqual(str(handler), "Handler for the 4 x 4 board")
        handler2 = Handler(8)
        self.assertEqual(str(handler2), "Handler for the 8 x 8 board")

    def test_equality(self):
        handler1 = Handler(8)
        handler2 = Handler(8)
        handler3 = Handler(4)
        self.assertEqual(handler1, handler2)
        self.assertNotEqual(handler1, handler3)

    def test_initiate_game(self):
        handler = Handler(2)
        handler.initiate_game()
        expected_list = [["white", "black"], ["black", "white"]]
        self.assertEqual(handler.board.get_board_list(), expected_list)

        handler2 = Handler(4)
        handler2.initiate_game()
        expected_list2 = [["empty", "empty", "empty", "empty"], \
            ["empty", "white", "black", "empty"],\
                ["empty", "black", "white", "empty"],\
                    ["empty", "empty", "empty", "empty"]]
        self.assertEqual(handler2.board.get_board_list(), expected_list2)

        handler3 = Handler(8)
        handler3.initiate_game()
        expected_list3 = [["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"], \
            ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],\
                ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"],\
                    ["empty", "empty", "empty", "white", "black", "empty", "empty", "empty"], \
                        ["empty", "empty", "empty", "black", "white", "empty", "empty", "empty"], \
                            ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"], \
                                ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"], \
                                    ["empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"]]
        self.assertEqual(handler3.board.get_board_list(), expected_list3)

def main():

    unittest.main(verbosity = 3)

if __name__ == "__main__":
    main()
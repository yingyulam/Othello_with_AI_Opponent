'''
Yingyu Lin
CS 5001, Fall 2021
Final Project, Milestone 3

'''

import unittest
from board import Board
from move_checker import Move_checker


class Test_move_checker(unittest.TestCase):

    def test_move_checker_init(self):
        board = Board(4)
        checker = Move_checker(board)
        self.assertEqual(checker.name, "Move_checker")
        self.assertEqual(checker.board_size, 4)
        expected = [["empty", "empty", "empty", "empty"], \
            ["empty", "empty", "empty", "empty"], \
                ["empty", "empty", "empty", "empty"], \
                    ["empty", "empty", "empty", "empty"]]
        self.assertEqual(checker.board_list, expected)

    def test_string_method(self):
        board = Board(8)
        checker = Move_checker(board)
        self.assertEqual(str(checker), "Move checker for a 8 x 8 board")

    def test_equality(self):
        board = Board(8)
        board2 = Board(4)
        checker1 = Move_checker(board)
        checker2 = Move_checker(board)
        checker3 = Move_checker(board2)
        self.assertEqual(checker1, checker2)
        self.assertNotEqual(checker1, checker3)

    def test_get_opponent_color(self):
        checker = Move_checker(Board(8))
        self.assertEqual(checker.get_opponent_color("black"), "white")
        self.assertEqual(checker.get_opponent_color("white"), "black")

    def test_get_increment(self):
        checker = Move_checker(Board(8))
        self.assertEqual(checker.get_increment("north"), (-1, 0))
        self.assertEqual(checker.get_increment("south"), (1, 0))
        self.assertEqual(checker.get_increment("west"), (0, -1))
        self.assertEqual(checker.get_increment("east"), (0, 1))
        self.assertEqual(checker.get_increment("northwest"), (-1, -1))
        self.assertEqual(checker.get_increment("northeast"), (-1, 1))
        self.assertEqual(checker.get_increment("southwest"), (1, -1))
        self.assertEqual(checker.get_increment("southeast"), (1, 1))

    def test_check(self):
        board = Board(4)
        board.update(1, 1, "white")
        board.update(1, 2, "black")
        board.update(2, 1, "black")
        board.update(2, 2, "white")
        checker = Move_checker(board)
        self.assertTrue(checker.check("black", 3, 2, "north"))
        self.assertTrue(checker.check("black", 0, 1, "south"))
        self.assertTrue(checker.check("black", 1, 0, "east"))
        self.assertTrue(checker.check("black", 2, 3, "west"))
        self.assertFalse(checker.check("black", 0, 0, "north"))

    def test_get_possible_direction(self):
        board = Board(8)
        checker = Move_checker(board)
        self.assertEqual(checker.get_possible_directions(0, 0), \
            ["east", "south", "southeast"])
        self.assertEqual(checker.get_possible_directions(0, 7), \
            ["west", "south", "southwest"])
        self.assertEqual(checker.get_possible_directions(1, 2), \
            ["west", "east", "south", "southwest", "southeast"])
        self.assertEqual(checker.get_possible_directions(7, 0), \
            ["north", "east", "northeast"])
        self.assertEqual(checker.get_possible_directions(7, 7), \
            ["north", "west", "northwest"])
        self.assertEqual(checker.get_possible_directions(7, 4), \
            ["west", "east", "north", "northwest", "northeast"])
        self.assertEqual(checker.get_possible_directions(2, 1), \
            ["north", "south", "east", "northeast", "southeast"])
        self.assertEqual(checker.get_possible_directions(3, 7), \
            ["north", "south", "west", "northwest", "southwest"])
        self.assertEqual(checker.get_possible_directions(4, 4), \
            ["north", "south", "west", "east", "northwest", \
                "northeast", "southwest", "southeast"])

    def test_is_legal(self):
        board = Board(4)
        board.update(1, 1, "white")
        board.update(1, 2, "black")
        board.update(2, 1, "black")
        board.update(2, 2, "white")
        checker = Move_checker(board)
        self.assertFalse(checker.is_legal("black", 0, 0))
        self.assertTrue(checker.is_legal("black", 0, 1))
        self.assertFalse(checker.is_legal("black", 0, 2))
        self.assertFalse(checker.is_legal("black", 0, 3))
        self.assertTrue(checker.is_legal("black", 1, 0))
        self.assertFalse(checker.is_legal("black", 1, 3))
        self.assertFalse(checker.is_legal("black", 3, 0))
        self.assertFalse(checker.is_legal("black", 3, 1))
        self.assertTrue(checker.is_legal("black", 3, 2))
        self.assertFalse(checker.is_legal("black", 3, 3))

        self.assertFalse(checker.is_legal("white", 0, 0))
        self.assertFalse(checker.is_legal("white", 0, 1))
        self.assertTrue(checker.is_legal("white", 0, 2))
        self.assertFalse(checker.is_legal("white", 0, 3))
        self.assertFalse(checker.is_legal("white", 1, 0))
        self.assertTrue(checker.is_legal("white", 1, 3))
        self.assertFalse(checker.is_legal("white", 3, 0))
        self.assertTrue(checker.is_legal("white", 3, 1))
        self.assertFalse(checker.is_legal("white", 3, 2))
        self.assertFalse(checker.is_legal("white", 3, 3))

    def test_record_positions(self):
        board = Board(8)
        board.update(3, 3, "white")
        board.update(3, 4, "black")
        board.update(4, 2, "white")
        board.update(4, 3, "black")
        board.update(4, 4, "black")
        board.update(5, 4, "black")
        checker = Move_checker(board)
        self.assertEqual(checker.record_positions("black", 3, 2), [(3, 3)])
        self.assertEqual(checker.record_positions("black", 4, 1), [(4, 2)])
        self.assertEqual(checker.record_positions("white", 3, 5), [(3, 4)])
        self.assertEqual(checker.record_positions("white", 4, 5), [(4, 4), (4, 3)])
        self.assertEqual(checker.record_positions("white", 5, 5), [(4, 4)])


        

def main():

    unittest.main(verbosity = 3)

if __name__ == "__main__":
    main()
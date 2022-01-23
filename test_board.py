import unittest
from board import Board

class TestBoard(unittest.TestCase):

    def test_init_board_basic(self):
        board = Board(2)
        self.assertEqual(board.name, "Board")
        self.assertEqual(board.board_size, 2)
        expected_board = [["empty", "empty"], ["empty", "empty"]]
        self.assertEqual(board.board, expected_board)
        self.assertTrue(board.is_player1)

    def test_init_board_not_integer(self):
        with self.assertRaises(TypeError):
            board = Board("board")
    
    def test_init_board_negative(self):
        with self.assertRaises(ValueError):
            board = Board(-4)
    
    def test_init_board_odd_integer(self):
        with self.assertRaises(ValueError):
            board = Board(5)

    def test_string(self):
        board = Board(4)
        self.assertEqual(str(board), "4 x 4 board")

    def test_equality_true(self):
        board1 = Board(4)
        board2 = Board(4)
        self.assertEqual(board1, board2)

    def test_equality_false(self):
        board1 = Board(4)
        board2 = Board(8)
        self.assertNotEqual(board1, board2)
    
    def test_equality_error(self):
        with self.assertRaises(TypeError):
            board = Board(4) == "Board"
    
    def test_create_board(self):
        board = Board(4)
        expected_board = [["empty", "empty", "empty", "empty"], \
            ["empty", "empty", "empty", "empty"], \
                ["empty", "empty", "empty", "empty"], \
                    ["empty", "empty", "empty", "empty"]]
        self.assertEqual(board.create_board(), expected_board)

    def test_update_basic(self):
        board = Board(4)
        board.update(2, 3, "black")
        expected_board = [["empty", "empty", "empty", "empty"], \
            ["empty", "empty", "empty", "empty"], \
                ["empty", "empty", "empty", "black"], \
                    ["empty", "empty", "empty", "empty"]]
        self.assertEqual(board.board, expected_board)
        self.assertFalse(board.is_player1)

    def test_update_row_not_integer(self):
        with self.assertRaises(TypeError):
            board = Board(4)
            board.update(2.2, 3, "black")

    def test_update_row_negative(self):
        with self.assertRaises(ValueError):
            board = Board(4)
            board.update(-1, 3, "black")

    def test_update_row_too_big(self):
        with self.assertRaises(ValueError):
            board = Board(4)
            board.update(4, 3, "black")

    def test_update_column_not_integer(self):
        with self.assertRaises(TypeError):
            board = Board(4)
            board.update(2, 3.3, "black")

    def test_update_column_negative(self):
        with self.assertRaises(ValueError):
            board = Board(4)
            board.update(2, -1, "black")

    def test_update_column_too_big(self):
        with self.assertRaises(ValueError):
            board = Board(4)
            board.update(2, 4, "black")

    def test_update_new_status_not_string(self):
        with self.assertRaises(TypeError):
            board = Board(4)
            board.update(2, 3, 0)

    def test_update_new_status_not_valid(self):
        with self.assertRaises(ValueError):
            board = Board(4)
            board.update(2, 3, "pink")

    def test_flip_tile_basic(self):
        board = Board(4)
        board.update(2, 3, "black")
        board.flip_tile(2, 3)
        expected_board = [["empty", "empty", "empty", "empty"], \
            ["empty", "empty", "empty", "empty"], \
                ["empty", "empty", "empty", "white"], \
                    ["empty", "empty", "empty", "empty"]]
        self.assertEqual(board.board, expected_board)

    def test_flip_tile_row_not_integer(self):
            with self.assertRaises(TypeError):
                board = Board(4)
                board.update(2, 3, "black")
                board.flip_tile(2.2, 3)

    def test_flip_tile_row_negative(self):
        with self.assertRaises(ValueError):
            board = Board(4)
            board.update(2, 3, "black")
            board.flip_tile(-1, 3)

    def test_flip_tile_row_too_big(self):
        with self.assertRaises(ValueError):
            board = Board(4)
            board.update(2, 3, "black")
            board.flip_tile(4, 3)

    def test_flip_tile_column_not_integer(self):
        with self.assertRaises(TypeError):
            board = Board(4)
            board.update(2, 3, "black")
            board.flip_tile(2, 3.3)

    def test_flip_tile_column_negative(self):
        with self.assertRaises(ValueError):
            board = Board(4)
            board.update(2, 3, "black")
            board.flip_tile(2, -1)

    def test_flip_tile_column_too_big(self):
        with self.assertRaises(ValueError):
            board = Board(4)
            board.update(2, 3, "black")
            board.flip_tile(2, 4)


    def switch_player_True_to_False(self):
        board = Board(4)
        board.switch_player()
        self.assertFalse(board.is_player1)

    def switch_player_False_to_True(self):
        board = Board(4)
        board.switch_player()
        board.switch_player()
        self.assertTrue(board.is_player1)

    def test_get_cell_status_basic(self):
        board = Board(4)
        self.assertEqual(board.get_cell_status(2, 3), "empty")

    def test_get_cell_status_row_not_integer(self):
        with self.assertRaises(TypeError):
            board = Board(4)
            board.get_cell_status(2,2, 3)

    def test_get_cell_status_row_negative(self):
        with self.assertRaises(ValueError):
            board = Board(4)
            board.get_cell_status(-1, 3)
        
    def test_get_cell_status_row_too_big(self):
        with self.assertRaises(ValueError):
            board = Board(4)
            board.get_cell_status(4, 3)
    
    def test_get_cell_status_column_not_integer(self):
        with self.assertRaises(TypeError):
            board = Board(4)
            board.get_cell_status(2, 3.3)

    def test_get_cell_status_column_negative(self):
        with self.assertRaises(ValueError):
            board = Board(4)
            board.get_cell_status(2, -1)

    def test_get_cell_status_column_too_big(self):
        with self.assertRaises(ValueError):
            board = Board(4)
            board.get_cell_status(2, 4)

    def test_is_empty_basic_empty(self):
        board = Board(4)
        self.assertTrue(board.is_empty(2, 3))

    def test_is_empty_basic_not_empty(self):
        board = Board(4)
        board.update(2, 3, "black")
        self.assertFalse(board.is_empty(2, 3))
    

    def test_is_empty_row_not_integer(self):
        with self.assertRaises(TypeError):
            board = Board(4)
            board.is_empty(2.2, 3)

    def test_is_empty_row_negative(self):
        with self.assertRaises(ValueError):
            board = Board(4)
            board.is_empty(-1, 3)

    def test_is_empty_row_too_big(self):
        with self.assertRaises(ValueError):
            board = Board(4)
            board.is_empty(4, 3)

    def test_is_empty_column_not_integer(self):
        with self.assertRaises(TypeError):
            board = Board(4)
            board.is_empty(2, 3.3)

    def test_is_empty_column_negative(self):
        with self.assertRaises(ValueError):
            board = Board(4)
            board.is_empty(2, -1)

    def test_is_empty_column_too_big(self):
        with self.assertRaises(ValueError):
            board = Board(4)
            board.is_empty(2, 4)

    def test_get_board_size(self):
        board = Board(4)
        self.assertEqual(board.get_board_size(), 4)

    def test_get_board_list(self):
        board = Board(4)
        expected_board = [["empty", "empty", "empty", "empty"], \
            ["empty", "empty", "empty", "empty"], \
                ["empty", "empty", "empty", "empty"], \
                    ["empty", "empty", "empty", "empty"]]
        self.assertEqual(board.get_board_list(), expected_board)

    def test_get_current_player_black(self):
        board = Board(4)
        self.assertEqual(board.get_current_player(), "black")

    def test_get_current_player_white(self):
        board = Board(4)
        board.switch_player()
        self.assertEqual(board.get_current_player(), "white")


    



def main():

    unittest.main(verbosity = 3)

if __name__ == "__main__":
    main()
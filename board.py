'''
Yingyu Lin
CS 5001, Fall 2021
Final Project, Milestone 1

This program creates a class Board that represents the status of each cell on 
the board. It belongs to Model.
'''
TWO = 2

from cell import Cell

class Board:
    def __init__(self, board_size):
        '''
        Constructor: create a new instance of Board_status
        Parameters: 
            self -- the current object
            n: an integer indicating the number of square in each 
                row/column of the board
        Errors:
            raise TypeError if board_size is not an integer
            raise ValueError if board_size is negative or odd
        '''
        if not isinstance(board_size, int):
            raise TypeError('board_size must be an integer')
        if board_size <= 0:
            raise ValueError('board_size must be a positve integer')
        if board_size % TWO != 0:
            raise ValueError('board_size must be an even number')

        self.board_size = board_size
        self.board = self.create_board()
        self.is_player1 = True


    def create_board(self):
        '''
        Method -- create_board()
            created a nested list containing the board information
        Parameter: self -- the current object
        Returns a nested list
            Each sublist indicates each row
            Each elements of the sublist corresponds to each column of the row.
        '''
        board = []
        for row in range(self.board_size):
            row_of_cells = []
            for column in range(self.board_size):
                row_of_cells.append(Cell())
            board.append(row_of_cells) 
        return board      


    def update(self, row, column, new_status):
        '''
        Method: update the status of one cell of the board
        Parameters: 
            self -- the current object
            row -- the row index of the cell to be updated
            column -- the column index of the cell to be updated
        Errors: 
            raise TypeError if row or column is not an integer
            raise ValueError if row or column is not between 0 and board size -1
            rasie ValueError if new_status is not empty, white or black
        '''
        if not isinstance(row, int):
            raise TypeError('row must be an integer')
        if row < 0 or row >= self.board_size:
            raise ValueError("row index out of range")
        if not isinstance(column, int):
            raise TypeError('column must be an integer')
        if column < 0 or column >= self.board_size:
            raise ValueError("column index out of range")
        if new_status not in ["empty", "white", "black"]:
            raise ValueError("new_status must be either empty, white or black")
        
        self.board[row][column].update_cell(new_status)
        self.switch_player()

    def switch_player(self):
        '''
        Method -- switch_player()
        Parameter:self -- the current object
        '''
        if self.is_player1:
            self.is_player1 = False
        elif not self.is_player1:
            self.is_player1 = True


    def get_status(self, row, column):
        '''
        Method -- get_status()
            get the status of the specified cell: black, white or empty
        Parameters: 
            self -- the current object
            row -- the row index of the cell to check
            column -- the column index of the cell to check
        returns a string representing the status of the cell ("black", "white",
            or "empty")
        Errors: 
            raise TypeError if row or column is not an integer
            raise ValueError if row or column is not between 0 and board size -1
        '''
        if not isinstance(row, int):
            raise TypeError('row must be an integer')
        if row < 0 or row >= self.board_size:
            raise ValueError("row index out of range")
        if not isinstance(column, int):
            raise TypeError('column must be an integer')
        if column < 0 or column >= self.board_size:
            raise ValueError("column index out of range")

        return self.board[row][column].get_cell_status()

    def is_empty(self, row, column):
        '''
        Method -- is_empty()
            check if the cell specified is empty
        Parameters:
            self -- the current object
            row -- the row index of the cell to check
            column -- the column index of the cell to check
        Returns a boolean; True if the cell is empty; false otherwise
        Errors: 
            raise TypeError if row or column is not an integer
            raise ValueError if row or column is not between 0 and board size -1
        '''
        if not isinstance(row, int):
            raise TypeError('row must be an integer')
        if row < 0 or row >= self.board_size:
            raise ValueError("row index out of range")
        if not isinstance(column, int):
            raise TypeError('column must be an integer')
        if column < 0 or column >= self.board_size:
            raise ValueError("column index out of range")
            
        return self.board[row][column].get_cell_status() == "empty"   

    def get_board_size(self):
        '''
        Method -- get_board_size()
        Parameter: self -- the current object
        Returns an integer indicating the size of the board
        '''
        return self.board_size

    def get_board_list(self):
        '''
        Method -- get_board_list()
        Parameter: self -- the current object
        Return a nested list containing all the board information
        '''
        return self.board

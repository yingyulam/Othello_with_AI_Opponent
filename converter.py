'''
Yingyu Lin
CS 5001, Fall 2021
Final Project, Milestone 3

This program creates a class Converter that converts between the index of cell 
(row, column) and x,y coordiantes on the screen. It belongs to Controller.
'''

TWO = 2
SQUARE = 50

class Converter:

    def __init__(self, board_size):
        '''
        Constructor -- creates a new instance of Converter
        Parameter:
            self -- the current object
            board_size -- an integer for the board size
        raise TypeError if board_size is not an integer
        raise ValueError if board_size is not a positive integer or not even
        '''
        if not isinstance(board_size, int):
            raise TypeError('board_size must be an integer')
        if board_size <= 0:
            raise ValueError('board_size must be a positive integer')
        if board_size % TWO != 0:
            raise ValueError('board_size must be an even number')
        
        self.name = "Converter"
        self.board_size = board_size


    def get_cell_coordinates(self, row, column):
        '''
        Method -- get_cell_coordinates()
            calculate the x,y coordinates of the enter of the cell 
        Parameters: 
            self -- the current object
            row -- an integer for the row index of the cell
            column -- an integer for the column index of the cell
        Returns the x,y coordinates of the center of the cell.
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

        center_x = -self.board_size*SQUARE/TWO + SQUARE/TWO + SQUARE*column
        center_y = self.board_size*SQUARE/TWO - SQUARE/TWO - SQUARE*row
        return center_x, center_y


    def convert_coordinates_to_index(self, x, y):
        '''
        Method -- convert_coordinates_to_index()
        Parameters: 
            self -- the current object
            x -- an integer or float for the x coordinate
            y -- an integer or float for the y coordinate
        Returns the row, column index of the cell
        Returns -1, -1 if row or column is out of range
        Errors:
            raise TypeError if x is not an integer or float
            raise TypeError if y is not an integer or float
        '''
        if not isinstance(x, int) and not isinstance(x, float):
            raise TypeError("x must be an integer or float")
        if not isinstance(y, int) and not isinstance(y, float):
            raise TypeError("y must be an integer or float")

        row = self.board_size / TWO - y / SQUARE
        column = x / SQUARE + self.board_size / TWO

        if row >= self.board_size or row < 0 or column >= self.board_size \
            or column < 0:
            return -1, -1
        if row >= 0:
            row = int(row)
        if column >= 0:
            column = int(column)
        return row, column

    def __str__(self):
        '''
        String method
        Parameters: self-- the current object
        '''
        return "converter for " + str(self.board_size) + " x " + \
            str(self.board_size) + " board"

    def __eq__(self, other):
        '''
        Equality method
        Paramters: 
            self-- the current object
            other -- another object to compare
        '''
        if not isinstance(other, Converter):
            raise TypeError("other must be a Converter")
        return self.board_size == other.board_size
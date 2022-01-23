'''
Yingyu Lin
CS 5001, Fall 2021
Final Project, Milestone 1

This program creates a class Counter that counts the number of black and white
tiles on the board. It belongs to Model.
'''
from board import Board

class Counter:  

    def __init__(self, board):
        '''
        Constructor -- creat a new instance of Counter
        Parameters: 
            self -- the current object
            board -- an instance of Board
        Errors:
            raise TypeError if board is not an instance of Board
        '''
        if not isinstance(board, Board):
            raise TypeError("board must be a Board")

        self.board = board
        self.white_count = self.count_tiles("white")
        self.black_count = self.count_tiles("black")

    def count_tiles(self, color):
        '''
        Method -- count_tiles()
            Count the number of tiles of specified color on the board
        Parameters: 
            self -- the current object
            color -- the color of tiles
        Returns an integer that represents the number of tiles of specified
            color on the board
        Errors:
            raise TypeError if color is not a string
            raise ValueError if color is not white or black
        '''
        if not isinstance(color, str):
            raise TypeError("color must be a string")
        if color not in ["white", "black"]:
            raise ValueError("tile color must be either white or black")

        count = 0
        board_list = self.board.get_board_list()
        for row_of_cells in board_list:
            for cell in row_of_cells:
                if cell.get_cell_status() == color:
                    count += 1
        return count

    def get_tile_count(self, color):
        '''
        Method -- get_tile_count()
        Parameter: self -- the current object
        Returns an integer representing the number of tiles of specified color
            on the board
        Errors:
            raise TypeError if color is not a string
            raise ValueError if color is not white or black
        '''
        if not isinstance(color, str):
            raise TypeError("color must be a string")
        if color not in ["white", "black"]:
            raise ValueError("tile color must be either white or black")
            
        if color == "white":
            return self.white_count
        elif color == "black":
            return self.black_count




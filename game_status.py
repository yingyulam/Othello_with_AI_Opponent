'''
Yingyu Lin
CS 5001, Fall 2021
Final Project, Milestone 1

This program creates a class Game_status that determine the status of the game.
It belongs to Model.
'''

from board import Board
from move_checker import Move_checker

class Game_status:
    
    def __init__(self, board):
        '''
        Constructor -- create a new instance of Game_status
        Parameter: 
            self -- the current object
            board -- an instance of Board
        rasie TypeError if board is not an instance of Board
        '''
        if not isinstance(board, Board):
            raise TypeError('Board must be a Board')
            
        self.board = board
        self.board_size = self.board.get_board_size()
        self.white_count = self.count_tiles("white")
        self.black_count = self.count_tiles("black")
        self.move_checker = Move_checker(self.board)

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
                if cell == color:
                    count += 1
      
        return count


    def get_tile_count(self, color):
        '''
        Method -- get_tile_count()
        Parameter: 
            self -- the current object
            color -- a string for the color of the tile to count
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



    def is_gameover(self):
        '''
        Method -- is_gameover() 
            Check if the game is over
        Parameter: self -- the current object
        Returns a boolean; True if the game is over, False otherwise
        '''

        if self.white_count + self.black_count == \
            self.board_size * self.board_size:
            return True
            
        else:
            for row in range(self.board_size):
                for column in range(self.board_size):
                    if self.board.is_empty(row, column):

                        if self.board.is_player1 and self.move_checker.\
                            is_legal("black", row, column):
                            return False

                        elif (not self.board.is_player1) and self.move_checker.\
                            is_legal("white", row, column):
                            return False
            return True


    def check_winner(self):
        '''
        Method -- check_winner()
            Check the winner: "white", "black" or "tie"
        Parameter: self -- the current object
        Returns a string representing the winner or tie
        '''
 
        if self.white_count > self.black_count:
            return "white"
        elif self.black_count > self.white_count:
            return "black"
        else:
            return "tie"


    def get_winner_count(self):
        '''
        Method -- get_winner_count()
            Check how many tiles the winner has on the board
        Parameter: self -- the current object
        Returns an integer that represents of the number of tiles the winner has
        '''

        winner = self.check_winner()
        if winner == "white" or winner == "tie":
            return self.white_count
        elif winner == "black":
            return self.black_count

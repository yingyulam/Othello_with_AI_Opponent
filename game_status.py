'''
Yingyu Lin
CS 5001, Fall 2021
Final Project, Milestone 1

This program creates a class Game_status that determine the status of the game.
It belongs to Model.
'''


from counter import Counter
from board import Board

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
        self.counter = Counter(self.board)
        self.board_size = self.board.get_board_size()
        self.white_count = self.counter.get_tile_count("white")
        self.black_count = self.counter.get_tile_count("black")

    def is_gameover(self):
        '''
        Method -- is_gameover() 
            Check if the game is over
        Parameter: self -- the current object
        Returns a boolean; True if the game is over, False otherwise
        '''

        return self.white_count + self.black_count == \
            self.board_size * self.board_size

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

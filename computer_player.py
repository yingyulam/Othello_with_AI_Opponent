'''
Yingyu Lin
CS 5001, Fall 2021
Final Project, Milestone 3

This program creates a class computer_player that plays white tile.
It belongs to Controller.
'''

import random
from board import Board
from move_checker import Move_checker
from terminal_tile import Terminal_tile
from terminal_board import Terminal_board
from converter import Converter

class Computer_player():

    def __init__(self, board):
        '''
        Constructor -- make a new instance of Computer_player
        Parameters: 
            self -- the current object
            board -- a Board object
        '''
        self.name = "Computer player"
        self.board = board
        self.board_size = self.board.get_board_size()
        self.converter = Converter(self.board_size)
        self.move_checker = Move_checker(self.board)
        self.terminal_board = Terminal_board(self.board_size)
        self.tile = Terminal_tile()

    def __str__(self):
        '''
        String method
        Parameters: self -- the current object
        '''
        return "Computer Player for a " + str(self.board_size) + " x " + \
            str(self.board_size) + " board"

    def __eq__(self, other):
        '''
        Equality method
        Parameters: 
            self -- the current object
            other -- another Computer_player object
        '''
        return self.board == other.board

    def find_legal_moves(self):
        '''
        Method -- find_legal_moves() 
        Parameters: self -- the current object
        return a list of legal moves, i.e. tuples for row and column pair
        '''
        legal_moves = []
        for row in range(self.board_size):
            for column in range(self.board_size):
                if self.board.is_empty(row, column):
                    if self.move_checker.is_legal("white", row, column):
                        legal_moves.append((row, column))
        
        return legal_moves

    
    def get_vital_positions(self):
        '''
        Method -- get_vital_positions()
        Parameters: self -- the current object
        Returns a dictionary for 3 categories of positions
        '''
        categories = ["corners", "edges", "danger_zone"]
        vital_positions = {key: [] for key in categories}
        
        vital_positions["corners"] = [(0,0), (0, self.board_size-1), \
            (self.board_size-1, 0), (self.board_size-1, self.board_size-1)]

        for column in range(1, self.board_size-1):
            vital_positions["edges"].append((0, column))
            vital_positions["edges"].append((self.board_size-1, column))

        for row in range(1, self.board_size):
            vital_positions["edges"].append((row, 0))
            vital_positions["edges"].append((row, self.board_size-1))

        for column in range(1, self.board_size-1):
            vital_positions["danger_zone"].append((1, column))
            vital_positions["danger_zone"].append((self.board_size-2, column))

        for row in range(1, self.board_size-1):
            vital_positions["danger_zone"].append((row, 1))
            vital_positions["danger_zone"].append((row, self.board_size-2))

        return vital_positions
        
    
    def choose_move(self):
        '''
        Method -- choose_move()
        Parameters: self -- the current object
        Returns a tuple for two integers (row and column index)
        '''
        legal_positions = self.find_legal_moves()
        vital_positions = self.get_vital_positions()

        if len(legal_positions) <= 0:
            return (-1, -1)

        if len(legal_positions) == 1:
            return legal_positions[0]

        elif len(legal_positions) > 1: 
            categories = ["corners", "edges", "danger_zone", "other"]
            available_moves = {key: [] for key in categories}
            for position in legal_positions:
                if position in vital_positions["corners"]:
                    available_moves["corners"].append(position)
                elif position in vital_positions["edges"]:
                    available_moves["edges"].append(position)
                elif position in vital_positions["danger_zone"]:
                    available_moves["danger_zone"].append(position)
                else:
                    available_moves["other"].append(position)
    

            if len(available_moves["corners"]) >= 1:
                return random.choice(available_moves["corners"])

            elif len(available_moves["edges"]) >= 1:
                return random.choice(available_moves["edges"])
                    
            elif len(available_moves["other"]) >=1:
                return random.choice(available_moves["other"])
                    
            elif len(available_moves["danger_zone"]) >= 1:
                return random.choice(available_moves["danger_zone"])


    def play(self):
        '''
        Method -- play() 
        Parameters: self -- the current object 
        '''
        
        move = self.choose_move()
        if move != (-1, -1):
            row, column = move
            self.board.update(row, column, "white")
            self.place_one_tile(row, column)
            positions = self.move_checker.record_positions("white", row, column)
            for position in positions:
                (row_to_flip, column_to_flip) = position
                self.board.flip_tile(row_to_flip, column_to_flip)
                self.place_one_tile(row_to_flip, column_to_flip)



    def place_one_tile(self, row, column):
        '''
        Method -- place_one_tile()
        Parameter: 
            self -- the current object
            row -- an integer for the row index of the tile
            column -- an integer for the column index of the tile.
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

        color = self.board.get_cell_status(row, column)
        center_x, center_y = self.converter.get_cell_coordinates(row, column)
        self.tile.set_color(color)
        self.tile.draw_tile(center_x, center_y)



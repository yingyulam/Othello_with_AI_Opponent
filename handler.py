'''
Yingyu Lin
CS 5001, Fall 2021
Final Project, Milestone 3

This program creates a class Handler that communicate between model and view.
It belongs to Controller.
'''
import random
from board import Board
from game_status import Game_status
from terminal_board import Terminal_board
from terminal_tile import Terminal_tile
from converter import Converter
from move_checker import Move_checker
from scores_file import Scores_file
from computer_player import Computer_player

TWO = 2
SQUARE = 50

class Handler:
    
    def __init__(self, board_size):
        '''
        Create a new instance of Controller
        Parameters:
            self -- the current object
            board -- a Board instance
        Errors:
            raise TypeError if board_size is not an integer
            raise ValueError if board_size is negative or odd
        '''
        if not isinstance(board_size, int):
            raise TypeError('board_size must be an integer')
        if board_size <= 0:
            raise ValueError('board_size must be a positive integer')
        if board_size % TWO != 0:
            raise ValueError('board_size must be an even number')
        
        self.name = "Handler"
        self.board = Board(board_size)
        self.board_size = self.board.get_board_size()
        self.tile = Terminal_tile()
        self.terminal_board = Terminal_board(self.board_size)
        self.converter = Converter(self.board_size)
        self.move_checker = Move_checker(self.board)
        self.computer_player = Computer_player(self.board)

    def __str__(self):
        '''
        String method
        Parameter: self -- the current object
        '''
        return "Handler for the " + str(self.board_size) + " x " + \
            str(self.board_size) + " board"

    
    def __eq__(self, other):
        '''
        Equality method
        Parameters: 
            self -- the current object
            other -- another Hanlder object
        '''
        if not isinstance(other, Handler):
            raise TypeError("other must be a Handler")

        return self.board == other.board


    def initiate_game(self):
        '''
        Method -- initiate_game()
            initiate the game by putting four tiles at the center of the board
        Parameter: self -- the current object
        '''
        self.terminal_board.draw_empty_board()
        self.board.update(int(self.board_size/2-1), int(self.board_size/2), "black")
        self.board.update(int(self.board_size/2-1), int(self.board_size/2-1), "white")
        self.board.update(int(self.board_size/2), int(self.board_size/2-1), "black")
        self.board.update(int(self.board_size/2), int(self.board_size/2), "white")
        self.terminal_board.announce_turn("black")
        self.render()

    def render(self):
        '''
        Method -- render()
            draw all the tiles to the board!
        Parameter: self -- the current object
        '''

        for row in range(self.board_size):

            for column in range(self.board_size):
                center_x, center_y = self.converter.get_cell_coordinates(row, column)

                if not self.board.is_empty(row, column):
                    color = self.board.get_cell_status(row, column)
                    self.tile.set_color(color)
                    self.tile.draw_tile(center_x, center_y)


    def get_click(self, x, y):
        '''
        method -- place_tile()
            this is a method for the onclick function. It will be called when
            the user clicks on the screen
        Parameters: 
            self -- the current object
            x -- the x coordinate that the user clicks on the screen
            y -- the y coordinate that the user clicks on the screen
            the values of x and y comes from the onclick function of turtle
        '''
        if not isinstance(x, int) and not isinstance(x, float):
            raise TypeError("x must be an integer or float")
        if not isinstance(y, int) and not isinstance(y, float):
            raise TypeError("y must be an integer or float")

        row, column = self.converter.convert_coordinates_to_index(x, y)

        if row != -1 and column != -1:
            if self.board.is_empty(row, column):

                if self.move_checker.is_legal("black", row, column):
                    self.board.update(row, column, "black")
                    self.place_one_tile(row, column)
                    positions = self.move_checker.record_positions("black", row, column)

                    for position in positions:
                        (row_to_flip, column_to_flip) = position
                        self.board.flip_tile(row_to_flip, column_to_flip)
                        self.place_one_tile(row_to_flip, column_to_flip)
                                       
                    game_status = Game_status(self.board)
                    if not game_status.is_gameover():
                        self.make_annoucement()
                        self.computer_player.play()
                        if not game_status.is_gameover():
                            self.make_annoucement()
                        else:
                            self.announce_winner()
                    else:
                        self.announce_winner()


    def make_annoucement(self):
        '''
        Method -- make_annoucement()
        Parameters: self -- the current object
        '''
        self.terminal_board.clear_message()
        color = self.board.get_current_player()
        self.terminal_board.announce_turn(color)


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


    def announce_winner(self):
        '''
        Method -- check_winner()
            check the winner of the game and pass the information to Terminal_
            message for printout
        Parameters: self -- the current object
        '''
        game_status = Game_status(self.board)

        if game_status.is_gameover():
            black_count = game_status.get_tile_count("black")
            winner = game_status.check_winner()
            winner_count = game_status.get_winner_count()
            self.terminal_board.set_winner(winner)
            self.terminal_board.clear_message()
            self.terminal_board.print_winner(winner_count)
            self.terminal_board.announce_winner(winner_count)
            self.tile.deregister_click()
            human_player_name = self.terminal_board.get_human_player_name()
            scores_file = Scores_file()
            scores_file.update(human_player_name, black_count)

            


    def get_click_place_tile(self):
        '''
        Method -- get_click_place_tile()
            Call the register_click function in the terminal_board to trigger 
            the get_click function
        Parmeter: self -- the current object
        '''
        self.tile.register_click(self.get_click)


 






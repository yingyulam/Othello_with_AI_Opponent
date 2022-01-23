'''
Yingyu Lin
CS 5001, Fall 2021
Final Project, Milestone 1

This program creates a class Terminal_board to draw the board on the screen.
It belongs to View.
'''
TWO = 2
THREE = 3
SQUARE = 50
DEGREE = 90
SIDES = 4
RADIUS = 20
HEADING = 0
SPEED = 100

import turtle

class Terminal_board:

    def __init__(self, board_size):
        '''
        Constructor: create a new instance of Empty_board
        Parameters:
            self -- the current object
            board_size -- an integer for the size of the board
        Errors:
            raise TypeError if the board size is not an integer
            raise ValueError if the board size is the board size is not a 
                positive even integer
        '''
        if not isinstance(board_size, int):
            raise TypeError('board_size must be an integer')
        if board_size <= 0:
            raise ValueError('board_size must be a positive integer')
        if board_size % TWO != 0:
            raise ValueError('board_size must be an even number')
            
        self.board_size = board_size
        self.corner = -self.board_size * SQUARE / TWO
        self.pen = turtle.Turtle()
        self.pen.speed(SPEED)
        self.pen_for_message = turtle.Turtle()
        self.pen.hideturtle()
        self.pen_for_message.speed(SPEED)
        self.pen_for_message.hideturtle()

    def draw_empty_board(self):
        '''
        Method -- draw_empty_board()
        Parameter: self -- the current object
        '''
    
        self.pen.setheading(HEADING)
        self.setup()
        self.draw_green_background()
        self.draw_horizontal_lines()
        self.draw_vertical_lines()      


    def setup(self):
        '''
        Method -- setup() 
            set up the background of the screen
        Parameters: 
            self -- the current object
        Returns: none
        '''
        turtle.setup(self.board_size * SQUARE + SQUARE, \
            self.board_size * SQUARE + THREE * SQUARE)
        turtle.screensize(self.board_size * SQUARE, self.board_size * SQUARE)
        turtle.bgcolor("white")


    def draw_green_background(self):
        ''' 
        Method -- draw_green_background()
            draw the outline and the green background of the board
        Parameter: self -- the current object
        '''
        self.pen.up()
        self.pen.color("black", "forest green")
        self.pen.setposition(self.corner, self.corner)
        self.pen.begin_fill()
        for index in range(SIDES):
            self.pen.down()
            self.pen.forward(SQUARE * self.board_size)
            self.pen.left(DEGREE)
        self.pen.end_fill()


    def draw_line(self):
        '''
        Method -- draw_line()
            draw a line of the same length of the board
        Parameter: self -- the current object
        '''
        self.pen.down()
        self.pen.forward(SQUARE * self.board_size)
        self.pen.up()


    def draw_horizontal_lines(self):
        '''
        Method -- draw_horizontal_lines()
        Parameter: self -- the current object
        '''
        for index in range(1, self.board_size):
            self.pen.setposition(self.corner, (self.corner + SQUARE * index))
            self.draw_line()


    def draw_vertical_lines(self):
        '''
        Method -- draw_vertical_lines()
        Parameter: self -- the current object
        '''
        self.pen.left(DEGREE)
        for index in range(1, self.board_size):
            self.pen.setposition((self.corner + SQUARE * index), self.corner)
            self.draw_line()


    def announce_turn(self, opponent_color):
        '''
        Method -- annouce_turn()
            Announce the turn on the screen
        Parameters: 
            self -- the current object
            opponent_color -- a string for the color of the opponent
        Errors:
            raise TypeError if the opponent_color argument is not a string
            raise ValueError if the opponent_color argument is not black or white
        '''
        if not isinstance(opponent_color, str):
            raise TypeError('opponent_color must be a string')
        if opponent_color not in ["white", "black"]:
            raise ValueError("opponent_color must be either black or white")

        self.pen_for_message.up()
        self.pen_for_message.setposition(-SQUARE, self.board_size * \
            SQUARE / 2 + 1/2 * SQUARE)

        if opponent_color == "black":
            player = "White"
        elif opponent_color == "white":
            player = "Black"
        text = "Turn: " + player

        self.pen_for_message.down()
        self.pen_for_message.write(text, font = ("Arial", 16, "normal"))



    def set_winner(self, winner):
        '''
        Method -- set_winner()
        Parameter: 
            self -- the current object
            winner -- a string that presents the winner
        Errors: 
            raise ValueError if winner is not tie, white or black
        '''
        if winner not in ["tie", "white", "black"]:
            raise ValueError("Invalid winner")

        self.winner = winner


    def print_winner(self, winner_count):
        '''
        Method -- print_winner()
        Parameters: 
            self -- the current object
            winner_count -- an integer that represents the number of tile that 
                the winner has on the board
        Errors:
            raise TypeError if winner_count is not an integer
            raise ValueError if winner_count is not positive
        '''
        if not isinstance(winner_count, int):
            raise TypeError('winner_count must be an integer')
        if winner_count <= 0:
            raise ValueError("winner_count must be a positive integer")
            
        winner = self.winner.capitalize()
        if winner == "Tie":
            print("Game over!\nIt's a tie! "\
                "There are {} of each!".format(winner_count))
        else:
            print("Game over! {} Tiles win -- They have {} tiles!".\
                format(winner, winner_count))


    def announce_winner(self, winner_count):
        '''
        Method -- announce_winner()
        Parameters: 
            self -- the current object
            winner_count -- an integer for the tiles count of the winner
        Errors:
            raise TypeError if the winner_count argument is not an integer
            rasie ValueError if the winner_count argument is not greater than 2
        '''
        if not isinstance(winner_count, int):
            raise TypeError("winner_count must be and integer")
        if winner_count <= 2:
            raise ValueError("winner_count must be greater than 2")
        
        self.pen_for_message.up()
        self.pen_for_message.setposition(-2 * SQUARE, self.board_size * SQUARE / 2 + 1/2 * SQUARE)

        if self.winner == "tie":
            text = "Tie!" + " (" + str(winner_count) + " Tiles)"
        else:
            text = "Winner: " + self.winner.capitalize() + " (" + \
                str(winner_count) + " Tiles)"
        
        self.pen_for_message.down
        self.pen_for_message.write(text, font = ("Arial", 14, "normal"))


    def clear_message(self):
        '''
        Method -- clear_message()
            Erase the message from the message board
        Parameters: self -- the current object
        '''
        self.pen_for_message.clear()


    def get_winner_name(self):
        '''
        Method -- get_winner_name()
            Prompt the user to input the name of the winner
        Parameter: self -- the current object
        '''
        if self.winner == "tie":
            winner_name1 = input("Please enter the first player's name: ")
            winner_name2 = input("Please enter the second player's name: ")
            winner_list = [winner_name1, winner_name2]
        else:
            winner_name = input("Please enter the winner's name: ")
            winner_list = [winner_name]

        print("Thanks for playing Othello!")
        return winner_list
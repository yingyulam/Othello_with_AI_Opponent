'''
Yingyu Lin
CS 5001, Fall 2021
Final Project, Milestone 1

This program creates a class Terminal_board to draw the board on the screen.
It belongs to View.
'''
TWO = 2
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
            n -- an integer indicating # of squares in each row/column
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

    def draw_empty_board(self):
        '''
        Method -- draw_empty_board()
        Parameter: self -- the current object
        '''
        self.pen.hideturtle()
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
            self.board_size * SQUARE + SQUARE)
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
            self.pen.setposition(self.corner, self.corner + SQUARE * index)
            self.draw_line()


    def draw_vertical_lines(self):
        '''
        Method -- draw_vertical_lines()
        Parameter: self -- the current object
        '''
        self.pen.left(DEGREE)
        for index in range(1, self.board_size):
            self.pen.setposition(self.corner + SQUARE * index, self.corner, )
            self.draw_line()

    def register_click(self, fun):
        '''
        Method -- register_click()
        Parameters:
            self -- the current object
            fun -- a function to call when the user clicks on the screen
        '''
        screen = turtle.Screen()
        screen.onclick(fun)

    def deregister_click(self):
        '''
        Method -- register_click()
        Parameters: self -- the current object
        '''
        screen = turtle.Screen()
        screen.onclick(None)
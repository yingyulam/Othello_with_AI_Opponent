'''
Yingyu Lin
CS 5001, Fall 2021
Final Project, Milestone 3

This program creates a class Terminal_tile to draw a tile on the screen.
It belongs to View.
'''
SPEED = 100
RADIUS = 20
SQUARE = 50
HEADING = 0

import turtle

class Terminal_tile:

    def __init__(self):
        '''
        Constructor -- create a new instance of Terminal_tile
        Parameter: self -- the current object
        '''
        self.name = "Tile"
        self.radius = RADIUS
        self.color = "black"
        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        self.pen.speed(SPEED)

    def set_color(self, color):
        '''
        Method -- set_color()
            Change the color of the tile
        Parameter: 
            self -- the current object
            color -- the color of the tile
        Errors:
            raise ValueError if color is not white or black
        '''
        if color not in ["white", "black"]:
            raise ValueError("tile color must be either black or white")

        self.color = color

    def draw_tile(self, center_x, center_y):
        '''
        Method -- draw_tile()
            draw a tile on the specific location
        Parameters: 
            self -- the current object
            center_x -- the x coordinate of the cell to draw the tile
            center_y -- the y coordinate of the cell to draw the tile
        Errors:
            raise TypeError if center_x and cneter_y are not numbers
        '''
        if not isinstance(center_x, int) and not isinstance(center_x, float):
            raise TypeError("x must be an integer or float")
        if not isinstance(center_y, int) and not isinstance(center_y, float):
            raise TypeError("y must be an integer or float")

        x = center_x
        y = center_y - RADIUS
        self.pen.hideturtle()
        self.pen.setheading(HEADING)
        self.pen.up()
        self.pen.setposition(x, y)
        self.pen.color(self.color, self.color)
        self.pen.begin_fill()
        self.pen.down()
        self.pen.circle(RADIUS)
        self.pen.end_fill()
        self.pen.up() 


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


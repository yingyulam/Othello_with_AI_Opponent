'''
Yingyu Lin
CS 5001, Fall 2021
Final Project, Milestone 1

This program creates a class Cell that represents the cell on the board. It 
Belongs to Model.
'''

SQUARE = 50

class Cell:
    def __init__(self):
        '''
        Constructor: create a new instance of Cell
        Parameter: self -- the current object
        '''
        self.status = "empty"

    
    def update_cell(self, new_status):
        '''
        Method: update the satus of the Cell
        Parameters: 
            self -- the current object
            new_status -- the new status of the Cell, 
                only "empty", "black" and "white" are valid input.
        Errors: 
            raise ValueError if new_status is not empty or black or white
        '''
        if new_status not in ["empty", "white", "black"]:
            raise ValueError("new_status must be either empty, white or black")
        
        self.status = new_status

    def get_cell_status(self):
        '''
        Method: get the status of the cell
        Parameters: self -- the current object
        Returns a string representing the status of the cell
            Only "empty", "white" and "black" are valid
        '''
        return self.status

    def flip(self):
        '''
        Method -- flip()
            flip the status of the cell from black to white and vice versa
        Parameter: self -- the current object
        '''
        if self.status == "white":
            self.status = "black"
        elif self.status == "black":
            self.status = "white"

    def __str__(self):
        '''
        Method: string method to get the status of the cell
        Parameters: self -- the current object
        Returns a string representing the status of the cell.
        '''
        return self.status



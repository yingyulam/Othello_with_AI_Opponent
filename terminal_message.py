'''
Yingyu Lin
CS 5001, Fall 2021
Final Project, Milestone 1

This program creates a class Terminal_message to print the winning message to
the user. It belongs to view.
'''

class Terminal_message:

    def __init__(self):
        '''
        Constructor -- create a new instance of Terminal_message
        Parameter: self -- the current object
        '''
        #more attributes may needed when expanding the program
        self.winner = None

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

    def print_invalid_position(self):
        '''
        Method -- print_invalid_position()
        Parameter: self -- the current object
        '''
        print("Invalid position")
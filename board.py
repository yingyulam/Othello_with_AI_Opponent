'''
Yingyu Lin
CS 5001, Fall 2021
Final Project, Milestone 1

This program creates a class Board that represents the status of each cell on 
the board. It belongs to Model.
'''
TWO = 2

class Board:
    def __init__(self, board_size):
        '''
        Constructor: create a new instance of Board_status
        Parameters: 
            self -- the current object
            board_size: an integer for the number of squares in each 
                row/column of the board
        Atrributes: 
            board_size -- an integer for the size of the board
            board -- a nested list containning the status of each cell on 
                the board. Each element (cell) can be 1) empty; 2) having a 
                black tile; 3) having a white tile
            is_player1 -- whether the current player is player1 (black tile)
        Errors:
            raise TypeError if board_size is not an integer
            raise ValueError if board_size is negative or odd
        '''

        if not isinstance(board_size, int):
            raise TypeError('board_size must be an integer')
        if board_size <= 0:
            raise ValueError('board_size must be a positve integer')
        if board_size % TWO != 0:
            raise ValueError('board_size must be an even number')
            
        self.name = "Board"
        self.board_size = board_size
        self.board = self.create_board()
        self.is_player1 = True

    def __str__(self):
        '''
        Method -- string method
        Parameters: self -- the current object
        Returns a string for the board
        '''
        return str(self.board_size) + " x " + str(self.board_size) + " board"

    def __eq__(self, other):
        '''
        Method -- equality
        Parameters: 
            self -- the current object
            other -- an instance of Board
        returns a boolean; True if the size of the boards are the same
        '''
        if not isinstance(other, Board):
            raise TypeError('other must be a Board')
        return self.board_size == other.board_size

    def create_board(self):
        '''
        Method -- create_board()
            created a nested list containing the board information. Each cell is
            set to be empty initially.
        Parameter: self -- the current object
        Returns a nested list
            The index of the sublists indicate the row.
            The index of elements in each sublist indicates the column.
            Each element in represents the status of each cell of the board.
        '''
        board = []

        for row in range(self.board_size):
            row_of_cells = []
            for column in range(self.board_size):
                row_of_cells.append("empty")
            board.append(row_of_cells) 

        return board      


    def update(self, row, column, new_status):
        '''
        Method: update the status of one cell of the board
        Parameters: 
            self -- the current object
            row -- an integer for the row index of the cell to update
            column -- an integer for the column index of the cell to update
        Errors: 
            raise TypeError if row or column is not an integer
            raise ValueError if row or column is not between 0 and board size -1
            raise TypeError if new_status is not a string
            rasie ValueError if new_status is not empty, white or black
        '''

        if not isinstance(row, int):
            raise TypeError('row must be an integer')
        if row < 0 or row >= self.board_size:
            raise ValueError("row index out of range")
        if not isinstance(column, int):
            raise TypeError('column must be an integer')
        if column < 0 or column >= self.board_size:
            raise ValueError("column index out of range")
        if not isinstance(new_status, str):
            raise TypeError('new_status must be a string')
        if new_status not in ["empty", "white", "black"]:
            raise ValueError("new_status must be either empty, white or black")
        
        self.board[row][column] = new_status
        self.switch_player()


    def flip_tile(self, row, column):
        '''
        Method -- flip_tile()
            flip the tile in the cell specified. 
        Parameters: 
            self -- the current object
            row -- an integer for the row index of the cell to flip
            column -- an integer for the column index of the cell to flip
        '''
        if not isinstance(row, int):
            raise TypeError('row must be an integer')
        if row < 0 or row >= self.board_size:
            raise ValueError("row index out of range")
        if not isinstance(column, int):
            raise TypeError('column must be an integer')
        if column < 0 or column >= self.board_size:
            raise ValueError("column index out of range")

        tile_color = self.board[row][column]

        if tile_color == "white":
            self.board[row][column] = "black"
        elif tile_color == "black":
            self.board[row][column] = "white"
        


    def switch_player(self):
        '''
        Method -- switch_player()
        Parameter:self -- the current object
        '''

        if self.is_player1:
            self.is_player1 = False
        elif not self.is_player1:
            self.is_player1 = True


    def get_cell_status(self, row, column):
        '''
        Method -- get_status()
            get the status of the specified cell: black, white or empty
        Parameters: 
            self -- the current object
            row -- an integer for the row index of the cell to check
            column -- an integer for the column index of the cell to check
        returns a string representing the status of the cell ("black", "white",
            or "empty")
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

        return self.board[row][column]

    def is_empty(self, row, column):
        '''
        Method -- is_empty()
            check if the cell specified is empty
        Parameters:
            self -- the current object
            row -- an integer for the row index of the cell to check
            column -- an integer for the column index of the cell to check
        Returns a boolean; True if the cell is empty; false otherwise
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
            
        return self.board[row][column] == "empty"   

    def get_board_size(self):
        '''
        Method -- get_board_size()
        Parameter: self -- the current object
        Returns an integer indicating the size of the board
        '''
        return self.board_size


    def get_board_list(self):
        '''
        Method -- get_board_list()
        Parameter: self -- the current object
        Return a nested list containing all the board information
        '''
        return self.board

    
    def get_current_player(self):
        '''
        Method -- get_current_player()
        Parameters: self -- the current object
        '''
        if self.is_player1:
            return "black"
        else:
            return "white"


# def main():
#     board = Board(2)
#     print(board.board)

# main()

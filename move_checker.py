from board import Board

class Move_checker:

    def __init__(self, board):
        '''
        Constructor -- create a new instance of Move_checker
        Parameters:
            self -- the current object
            color -- a string for the color of the intended tile
            row -- a string for the intended row of the intended tile
            column -- a string for the intended column of the intended tile
        '''
        if not isinstance(board, Board):
            raise TypeError('board must be an instance of Board')

        self.board = board
        self.board_size = self.board.get_board_size()
        self.board_list = self.board.get_board_list()


    def get_opponent_color(self, color):
        '''
        Method -- get_opponent_color()
        Parameters: 
            self -- the current object
            color -- a string for the color of the intended tile
        Returns a string for the opponent's tile color
        Errors:
            rasie TypeError if the color argument is not a string
            raise ValueError if the color argument is not either black or white
        '''
        if not isinstance(color, str):
            raise TypeError('color must be a string')
        if color not in ["white", "black"]:
            raise ValueError('color must be either white or black')
            
        if color == "white":
            return "black"
        elif color == "black":
            return "white"


    def get_increment(self, direction):
        '''
        Method -- get_increment()
            get the increment of row and column index based on the checking
            direction.
        Parameters: 
            self -- the current object
            direction -- a string for the direction to check
        Returns a pair of integer for the increament of row and column index
        Errors:
            raise TypeError if the direction argument is not a string
            raise ValueError if the direction argument is not a valid direction
        '''
        if not isinstance(direction, str):
            raise TypeError('direction must be a string')
        if direction not in ["north", "south", "west", "east", "northwest", \
            "northeast", "southwest", "southeast"]:
            raise TypeError("invalid direction")

        if direction == "north":
            return -1, 0
        elif direction == "south":
            return 1, 0
        elif direction == "west":
            return 0, -1
        elif direction == "east":
            return 0, 1
        elif direction == "northwest":
            return -1, -1
        elif direction == "northeast":
            return -1, 1
        elif direction == "southwest":
            return 1, -1
        elif direction == "southeast":
            return 1, 1


    def check(self, color, row, column, direction):
        '''
        Method -- check()
            determine if a move can flip the opponent's tiles on the specified
            direction; check one direction per time.
        Parameters: 
            self -- the current object
            color -- a string for the tile color of the current player
            row -- a string for the row index of the intended move
            column -- a string for the column index of the intended move
            direction -- a string for the direction to check
        Returns a boolean:
            True if the move can flip the oppenent's tiles on the specified
            direction; false if the move cannot flip any opponent's tiles on the
            specified direction
        Errors:
            raise TypeError if the color argument is not a string
            raise ValueError if the color argument is not either white or black
            raise TypeError if the row argument is not an integer
            raise ValueError if the row argument is out of range
            raise TypeError if the column argument is not an integer
            raise ValueError if the column argument is out of range
            raise TypeError if the direction argument is not a string
            raise ValueError if the direction argument is not a valid direction
        '''
        if not isinstance(color, str):
            raise TypeError('color must be a string')
        if color not in ["white", "black"]:
            raise ValueError("new_status must be either white or black")
        if not isinstance(row, int):
            raise TypeError('row must be an integer')
        if row < 0 or row >= self.board_size:
            raise ValueError("row index out of range")
        if not isinstance(column, int):
            raise TypeError('column must be an integer')
        if column < 0 or column >= self.board_size:
            raise ValueError("column index out of range")
        if not isinstance(direction, str):
            raise TypeError('direction must be a string')
        if direction not in ["north", "south", "west", "east", "northwest", \
            "northeast", "southwest", "southeast"]:
            raise TypeError("invalid direction")

        row_increment, column_increment = self.get_increment(direction)
        opponent_color = self.get_opponent_color(color)
        adjacent_cell = self.board_list[row + row_increment]\
            [column + column_increment]
        if adjacent_cell == color or adjacent_cell == "empty":
            return False
        elif adjacent_cell == opponent_color:
            row_index = row + 2 * row_increment
            column_index = column + 2 * column_increment
            while row_index >= 0 and row_index <= self.board_size -1 \
                and column_index >= 0 and column_index <= self.board_size -1:
                cell_to_check = self.board_list[row_index][column_index]
                if cell_to_check == color:
                    return True
                elif cell_to_check == "empty":
                    return False
                elif cell_to_check == opponent_color:
                    row_index += row_increment
                    column_index += column_increment
            return False
            

    def get_possible_directions(self, row, column):
        '''
        Method: get_possible_directions()
            Determine the directions to check if a move is legal based on the 
            location of the intended move. For example, if the player intends
            to place a tile on the upper left corner, only the south, east and
            southeast need to be checked. 
        Parameters: 
            self -- the current object
            row -- an integer for the row index of the intended move
            column -- an integer for the column index of the intended move
        Returns a list containing the directions to be checked
        Errors:
            raise TypeError if the row argument is not an integer
            raise ValueError if the row argument is out of range
            raise TypeError if the column argument is not an integer
            raise ValueError if the column argument is out of range

        '''
        if not isinstance(row, int):
            raise TypeError('row must be an integer')
        if row < 0 or row >= self.board_size:
            raise ValueError("row index out of range")
        if not isinstance(column, int):
            raise TypeError('column must be an integer')
        if column < 0 or column >= self.board_size:
            raise ValueError("column index out of range")

        if row <= 1 and column <= 1: 
            return ["east", "south", "southeast"]
        elif row <= 1 and column >= self.board_size - 2:
            return ["west", "south", "southwest"]
        elif row <= 1 and column > 1 \
            and column < self.board_size - 2:
            return ["west", "east", "south", "southwest", "southeast"]
        elif row >= self.board_size - 2 and column <= 1: 
            return ["north", "east", "northeast"]
        elif row >= self.board_size - 2 \
            and column >= self.board_size - 2:
            return ["north", "west", "northwest"]
        elif row >= self.board_size - 2 \
            and column > 1 and column < self.board_size - 2:
            return ["west", "east", "north", "northwest", "northeast"]
        elif row > 1 and row < self.board_size - 2 \
            and column <= 1: 
            return ["north", "south", "east", "northeast", "southeast"]
        elif row > 1 and row < self.board_size - 2 \
            and column >= self.board_size - 2:
            return ["north", "south", "west", "northwest", "southwest"]
        else:
            return ["north", "south", "west", "east", "northwest", \
                "northeast", "southwest", "southeast"]


    def is_legal(self, color, row, column):
        '''
        Method -- is_legal()
            determine if a move is legal
        Parameters:
            self -- the current object
            color -- a string for the tile color of the current player
            row -- a string for the row index of the intended move
            column -- a string for the column index of the intended move
        Returns a bolean indicating if a move is legal
        Errors:
            raise TypeError if the color argument is not a string
            raise ValueError if the color argument is not either white or black
            raise TypeError if the row argument is not an integer
            raise ValueError if the row argument is out of range
            raise TypeError if the column argument is not an integer
            raise ValueError if the column argument is out of range
        '''
        if not isinstance(color, str):
            raise TypeError('color must be a string')
        if color not in ["white", "black"]:
            raise ValueError("new_status must be either white or black")
        if not isinstance(row, int):
            raise TypeError('row must be an integer')
        if row < 0 or row >= self.board_size:
            raise ValueError("row index out of range")
        if not isinstance(column, int):
            raise TypeError('column must be an integer')
        if column < 0 or column >= self.board_size:
            raise ValueError("column index out of range")
        
        for direction in self.get_possible_directions(row, column):
            if self.check(color, row, column, direction):
                return True


    def record_positions(self, color, row, column):
        '''
        Method -- record_position()
            record the positions of the tiles to be flipped
        Parameters:
            self -- the current object
            color -- a string for the tile color of the current player
            row -- a string for the row index of the intended move
            column -- a string for the column index of the intended move
        Returns a list containing all the positions of tiles to be flipped
        Errors:
            raise TypeError if the color argument is not a string
            raise ValueError if the color argument is not either white or black
            raise TypeError if the row argument is not an integer
            raise ValueError if the row argument is out of range
            raise TypeError if the column argument is not an integer
            raise ValueError if the column argument is out of range
        '''
        if not isinstance(color, str):
            raise TypeError('color must be a string')
        if color not in ["white", "black"]:
            raise ValueError("new_status must be either white or black")
        if not isinstance(row, int):
            raise TypeError('row must be an integer')
        if row < 0 or row >= self.board_size:
            raise ValueError("row index out of range")
        if not isinstance(column, int):
            raise TypeError('column must be an integer')
        if column < 0 or column >= self.board_size:
            raise ValueError("column index out of range")

        positions = []
        for direction in self.get_possible_directions(row, column):
            if self.check(color, row, column, direction):

                row_increment, column_increment = self.get_increment(direction)
                row_index = row + row_increment
                column_index = column + column_increment
                cell_status = self.board_list[row_index][column_index]
                while cell_status != color:
                    if (row_index, column_index) not in positions:
                        positions.append((row_index, column_index))
                    row_index += row_increment
                    column_index += column_increment
                    cell_status = self.board_list[row_index][column_index]
        
        return positions







        




                    


        








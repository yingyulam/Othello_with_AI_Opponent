'''
Yingyu Lin
CS 5001, Fall 2021
Final Project, Mileston 1

This is a program to place tiles on a 4x4 board.
'''

from handler import Handler


def main():
    try:
        board_size = 8
        handler = Handler(board_size)
        handler.initiate_game()
        handler.get_click_place_tile()

    except FileNotFoundError:
        raise FileNotFoundError("file {} does not exist".format(self.filename))
    except PermissionError:
        raise PermissionError("you do not have permission to use {}".\
            format(self.filename))
    except OSError as ex:
        raise OSError("Something went wrong while reading the file {}".\
            format(self.filename))

if __name__ == '__main__':
    main()

'''
Yingyu Lin
CS 5001, Fall 2021
Final Project, Mileston 1

This is a program to place tiles on a 4x4 board.
'''

from handler import Handler
from board import Board


def main():
    board_size = 4
    handler = Handler(board_size)
    handler.initiate_game()
    handler.get_click_place_tile()

if __name__ == '__main__':
    main()

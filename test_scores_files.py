'''
Yingyu Lin
CS 5001, Fall 2021
Final Project, Milestone 3

'''

import unittest
from scores_file import Scores_file

class Test_scores_file(unittest.TestCase):

    def test_scores_file_init(self):
        scores = Scores_file()
        self.assertEqual(scores.name, "Scores File")
        self.assertEqual(scores.filename, "scores.txt")

    def test_download_file(self):
        scores = Scores_file()
        self.assertEqual(scores.download_file(), "")

    def test_convert_scores_to_file(self):
        scores = Scores_file()
        self.assertEqual(scores.convert_scores_to_list(), [])

    def test_update(self):
        scores = Scores_file()
        scores.update("Rain", 45)
        self.assertEqual(scores.convert_scores_to_list(), [["Rain", "45"]])

def main():

    unittest.main(verbosity = 3)

if __name__ == "__main__":
    main()
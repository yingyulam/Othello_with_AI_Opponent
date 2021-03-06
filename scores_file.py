'''
Yingyu Lin
CS 5001, Fall 2021
Final Project, Milestone 3

This program creates a class Scores_file that prompt the user for name and store 
the game score records. It belongs to View.
'''

class Scores_file:
    
    def __init__(self):
        '''
        Constructor -- creates a new instance of Scores_file
        Parameters: self -- the current object
        '''
        self.name = "Scores File"
        self.filename = "scores.txt"
        self.scores_list = self.convert_scores_to_list()


    def download_file(self):
        '''
        Method -- download_file()
        Parameters: self -- the current object
        Returns a string for all the content in the file
        '''
        try:
            scores_file = open(self.filename, "r")
            scores_record = scores_file.read()
            scores_file.close()
            return scores_record

        except FileNotFoundError:
            raise FileNotFoundError("file {} does not exist".format(self.filename))
        except PermissionError:
            raise PermissionError("you do not have permission to use {}".\
                format(self.filename))
        except OSError as ex:
            raise OSError("Something went wrong while reading the file {}".\
                format(self.filename))


    def convert_scores_to_list(self):
        '''
        Method -- convert_scores_to_list()
        Parameter: self -- the current object
        Returns a list containing all the winners and their scores
        '''
        scores_list = []
        scores_string = self.download_file()
        if len(scores_string) > 0:
            scores_list_untreated = scores_string.split("\n")

            for name_score_string in scores_list_untreated:
                if len(name_score_string) > 0:
                    name_score_pair = name_score_string.split(" ")
                    scores_list.append(name_score_pair)
        
        return scores_list

    
    def update(self, human_player_name, human_player_score):
        '''
        Method -- update()
            update the scores file
        Parameters: 
            self -- the current object
            winner_name_list -- a list for the winner name(s)
            winner_score -- an integer for the winner score
        Errors: 
            raise TypeError if the winner_name_list argument is not a list
            raise TypeError if the winner_score argument is not an integer
            raise ValueError if the winner_score argument is not greater than 2
        '''
        if not isinstance(human_player_name, str):
            raise TypeError('winner_name_name must be a str')
        if not isinstance(human_player_score, int):
            raise TypeError('winner_score must be an integer')
        if human_player_score <= 2:
            raise ValueError("winner score must be greater than 2")  

        if len(self.scores_list) <= 0 or human_player_score < int(self.scores_list[0][-1]):
            self.scores_list.append([human_player_name, str(human_player_score)])
        
        elif human_player_score >= int(self.scores_list[0][-1]):
            self.scores_list.insert(0, [human_player_name, str(human_player_score)])  
        
        self.upload_file()



    def upload_file(self):
        '''
        Method -- upload_file()
        Parameters: self -- the current object
        '''
        try:
            scores_file = open(self.filename, "w")
            for name_score_pair in self.scores_list:
                name_score_string = " ".join(name_score_pair)
                scores_file.write(name_score_string)
                scores_file.write("\n")
            scores_file.close()
        except FileNotFoundError:
            raise FileNotFoundError("file does not exist")
        except PermissionError:
            raise PermissionError("you do not have permission to use this file")
        except OSError as ex:
            raise OSError("Something went wrong while reading the file")


#!/usr/bin/env python
"""
Create a python script in which you define a Class called Song, that Class will display the lyrics of a song.
The __init __ () method should have two arguments namely: 'self' and 'text'. 'text' is a list.
Within your Class, create a method / function called 'sing' that prints each element of the lyrics on its own line.
Define a variable: 'birthday song' that instantiates an object from the Class.
"""

__author__ = "Timo Verbist"
__email__ = "timo.verbist@student.kdg.be"
__status__ = "Development"

# import


class Song:  #class

    # function that initialises itself and the variable lst
    def __init__(self, lst):
        self.lst = lst

    # function that fills in the lines of the song with the words given in if __name__ == '__main__'
    # and prints out these lines under each other
    def sing(self):
        line1 = self.lst[0] + " " + self.lst[1] + " " + self.lst[2] + " " + self.lst[3]
        line2 = self.lst[0] + " " + self.lst[1] + " " + self.lst[4] + " " + self.lst[5]
        print(line1 + "\n" + line1 + "\n" + line2 + "\n" + line1)


if __name__ == '__main__':  # carries out the main function in the script "4) song.py"
    # These are the words that will be printed out on the different lines.
    birthdaysong = Song(["Happy", "birthday", "to", "you", "dear", "Jakob"])
    # this calls out the function in the class that prints out the lines.
    birthdaysong.sing()
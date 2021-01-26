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


class Song:

    def __init__(self, lst):
        self.lst = lst

    def sing(self):
        line1 = self.lst[0] + " " + self.lst[1] + " " + self.lst[2] + " " + self.lst[3]
        line2 = self.lst[0] + " " + self.lst[1] + " " + self.lst[4] + " " + self.lst[5]
        print(line1 + "\n" + line1 + "\n" + line2 + "\n" + line1)


if __name__ == '__main__':  # code to execute if called from command-line
    birthdaysong = Song(["Happy", "birthday", "to", "you", "dear", "Jakob"])
    birthdaysong.sing()
#!/usr/bin/env python
"""
Info about our project comes here
"""

__author__ = "Timo Verbist"
__email__ = "timo.verbist@student.kdg.be"
__status__ = "Development"

import random, string


def main():
    while True:
        print("We gaan een random wachtwoord genereren.")
        aantal = int(input("Hoeveel tekens wilt u in uw wachtwoord?\n"))
        print("\nopties:")
        print("1) Alleen cijfers")
        print("2) Alleen letters (klein + groot)")
        print("3) letters + andere tekens")
        print("4) combinatie van alles")
        keuze = int(input("geef uw keuze:\n"))
        print("")

        if keuze == 1:
            for i in range(aantal):
                print(random.randint(0, 9), end="")
        elif keuze == 2:
            for i in range(aantal):
                print(random.choice(string.ascii_letters), end="")
        elif keuze == 3:
            for i in range(aantal):
                print(random.choice(string.ascii_letters + "!@#$%^&*()_"), end="")
        elif keuze == 4:
            for i in range(aantal):
                print(random.choice(string.ascii_letters + string.digits + "!@#$%^&*()_"), end="")

        print("\n")


if __name__ == '__main__':  # code to execute if called from command-line
    main()

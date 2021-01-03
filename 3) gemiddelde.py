#!/usr/bin/env python
"""
Info about our project comes here
"""

__author__ = "Timo Verbist"
__email__ = "timo.verbist@student.kdg.be"
__status__ = "Development"


def main():
    data = 0
    while data != "!":
        i = 0
        totaal = 0
        data = 0
        lijst = []
        print("We berekenen hier het gemiddelde van 20 getallen van uw data.")
        print("Geef 20 getallen van de data in (! om te stoppen)")
        while i < 20 and data != "!":
            totaal += int(data)
            data = input("")
            if data != "!":
                lijst.append(data)
            i += 1
        if data != "!" or totaal !=0:
            print(totaal)
            gem = totaal/20
            print(gem)
            print(lijst)
            print("")
    print("einde")


if __name__ == '__main__':  # code to execute if called from command-line
    main()

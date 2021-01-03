#!/usr/bin/env python
"""
Het script vraagt de gebruiker om 2 natuurlijke getallen in te geven en
Deze 2 natuurlijke getallen te vermeerderen, verminderen, vermenigvuldigen of delen
"""

__author__ = "Timo Verbist"
__email__ = "timo.verbist@student.kdg.be"
__status__ = "finished"

# import


def main():
    print("We gaan 2 getallen vermenigvuldigen, delen, optellen of aftrekken")
    while True:
        getal1 = int(input('Geef getal1\n'))
        getal2 = int(input('Geef getal2\n'))
        teken = str(input('kies vermenigvuldigen(*), delen(/), optellen(+) of aftrekken(-)\n'))
        if teken == "*":
            maal = getal1 * getal2
            print(maal)
        elif teken == "/":
            deel = getal1 / getal2
            print(deel)
        elif teken == "+":
            plus = getal1 + getal2
            print(plus)
        elif teken == "-":
            min = getal1 - getal2
            print(min)


if __name__ == '__main__':  # code to execute if called from command-line
    main()

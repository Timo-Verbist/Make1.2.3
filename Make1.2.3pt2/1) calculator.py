#!/usr/bin/env python
"""

A re-make of your calculator that conforms to flow control.
You ask the user for 2 numbers
You ask the user to enter an operation
You give correct output
Your custom calculator now fully customized / improved with the right imports, functions and flow control.
"""

__author__ = "Timo Verbist"
__email__ = "timo.verbist@student.kdg.be"
__status__ = "finished"


# number1 = 0
# number2 = 0


def main():
    print("We're going to multiplicate, devide, add or subtract two numbers")

    while True:
        sign = str(input('Choose multiplication(*), division(/), addition(+) or subtraction(-)   (q to quit)\n'))
        if sign != "*" and sign != "/" and sign != "+" and sign != "-" and sign != "q":
            print("not a valid sign!\n")
            main()
        elif sign == "q":
            quit()

        try:
            number1 = int(input('Give number1\n'))
        except:
            print("this is not a natural number!\n")
            main()

        try:
            number2 = int(input('Give number2\n'))
        except:
            print("this is not a natural number!\n")
            main()

        if sign == "*":
            outcome = multiplication(number1, number2)
        elif sign == "/":
            outcome = division(number1, number2)
        elif sign == "+":
            outcome = addition(number1, number2)
        elif sign == "-":
            outcome = subtraction(number1, number2)
        elif sign == "q":
            quit()
        print("The outcome is", outcome, "\n")


def multiplication(number1, number2):
    return number1 * number2


def division(number1, number2):
    return number1 / number2


def addition(number1, number2):
    return number1 + number2


def subtraction(number1, number2):
    return number1 - number2


if __name__ == '__main__':  # code to execute if called from command-line
    main()

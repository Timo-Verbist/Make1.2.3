#!/usr/bin/env python
"""
Create a function that puts data (e.g. from a sensor) in a list.
There are always 20 items in the list, the average is printed.
Make sure you can interrupt the loop with a symbol / letter / number / ...
"""

__author__ = "Timo Verbist"
__email__ = "timo.verbist@student.kdg.be"
__status__ = "Development"


total = 0
mean = 0
lst = 0
i = 0


def main():
    data = 0
    while data != "!":
        global total
        global lst
        global mean
        global i
        i = 0
        total = 0
        data = 0
        lst = []
        print("We calculate here the mean of 20 numbers of your data.")
        print("Give 20 numbers of the data (! to stop)")
        while i < 20 and data != "!":
            total += int(data)
            data = input("")
            try:
                isinstance(int(data), int)
            except:
                if data == "!":
                    if i == 0:
                        i = 1
                    calculate_mean()
                    print_variables()
                    print("end")
                    quit()
                else:
                    print("This is invalid input!\n")
                    main()
            if data != "!":
                    lst.append(data)
            i += 1


def calculate_mean():
    global total
    global mean
    global i
    mean = total / i
    return mean


def print_variables():
    global total
    global mean
    global lst
    print(total)
    print(mean)
    print(lst)
    print("")


if __name__ == '__main__':  # code to execute if called from command-line
    main()

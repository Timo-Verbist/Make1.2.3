#!/usr/bin/env python
"""
Create a function that puts data (e.g. from a sensor) in a list.
There are always 20 items in the list, the average is printed.
Make sure you can interrupt the loop with a symbol / letter / number / ...
"""

__author__ = "Timo Verbist"
__email__ = "timo.verbist@student.kdg.be"
__status__ = "Development"

# declaration of the variables
total = 0
mean = 0
lst = 0
i = 0


def main():
    # reset data to zero
    data = 0
    # while loop until input is "!"
    while data != "!":
        # global is used to get the same value of the variable in the different functions
        global total
        global lst
        global mean
        global i
        # reset these variables to zero (and empty list) in the beginning of the loop
        i = 0
        total = 0
        data = 0
        lst = []
        print("We calculate here the mean of 20 numbers of your data.")
        print("Give 20 numbers of the data (! to stop)")
        # this asks the user for input 20 times, adds this to a list and adds this to a total.
        while i < 20 and data != "!":
            total += int(data)
            data = input("")
            try:
                isinstance(int(data), int)
            except:
                # if the user gives something else than an int:
                # if it's a "!", the functions "calculate_mean()" and "print_variables()" will be carried out
                # end the program will stop (quit)
                if data == "!":
                    # i can't be 0, otherwise x/0 gives an error
                    if i == 0:
                        i = 1
                    calculate_mean()
                    print_variables()
                    print("end")
                    quit()
                # if it's something else, (s)he'll get a message and start the main function again.
                else:
                    print("This is invalid input!\n")
                    main()
            # This way only numbers will be added to the list
            if data != "!":
                    lst.append(data)
            i += 1


# functions:


def calculate_mean():  # calculates the mean of the data and returns it
    # global is used to get the same value of the variable in the different functions
    global total
    global mean
    global i
    mean = total / i
    return mean


def print_variables():  # prints out the variables "total", "mean" and "lst"
    # global is used to get the same value of the variable in the different functions
    global total
    global mean
    global lst
    print(total)
    print(mean)
    print(lst)
    print("")


if __name__ == '__main__':  # carries out the main function in the script "3) mean.py"
    main()

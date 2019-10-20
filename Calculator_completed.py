# ======================================
# Import and Define Necessary Objects and Mode
# ======================================
import operator
import sys
operators = ['-','+','/','*','^']
opDict = {'^':operator.pow, '/':operator.truediv, '*':operator.mul, '+':operator.add, '-':operator.sub}
equation = 0
file = ''
style = 0

while style != "1" and style != "2":
    style = input("Please input 1 for file_read and 2 for interactive: ")

# ======================================
# The Caluclator Function
# ======================================
def recursive_calc(equation):
    """
                    A calculator that will recursively parse a string and evaluate as float. Acceptable operators are +,-,*,/,^.
    """
    # base case
    if equation.isdigit():
        return float(equation)
    #recursive case
    else:
        for operator in operators:
            # What if operator isnt present
            if operator not in equation:
                continue
            else:
                separated = equation.split(operator, maxsplit = 1)
                return opDict[operator](recursive_calc(separated[0]), recursive_calc(separated[1]))

# ======================================
# File Read 
# ======================================
if style == "1":
    print(""" File Read Mode Selected """)
    count = 0
    while file != 'quit':
        try:
            file = input('Please input your path to file here: ')
            if file == 'quit':
                continue
            file = open(file,'r')
            eq_set = file.readlines()
            for i in range(len(eq_set)):
                count += 1
                eq_set[i] = eq_set[i].replace("\n", "")
                eq_set[i] = eq_set[i].replace(" ", "")
                eval = recursive_calc(eq_set[i])
                print("Expression #", count , ': ', eval)
        except IOError:
            print("Unable to locate or access file, please try again")
        except TypeError:
            print('Please do not end your equation with an operator, try again.')
    print("""
                    ~~~~~~~~~~~~~~~~~~~~~~
                    Thanks for stopping by!
                    ~~~~~~~~~~~~~~~~~~~~~~
    """)

# ======================================
# Interactive Mode
# ======================================
if style == "2":
    print(""" Interactive Mode Selected """)
    while equation != 'quit':
        equation = input("Enter Expression Here, type 'quit' to exit: ")
        if equation == 'quit':
            continue
        equation = equation.replace(" ","")
        try:
            eval = recursive_calc(equation)
            print('Evaluated: ', eval)
        except TypeError:
            print('Please do not end your equation with an operator, try again.')
    print("""
                    ~~~~~~~~~~~~~~~~~~~~~~
                    Thanks for stopping by!
                    ~~~~~~~~~~~~~~~~~~~~~~
    """)
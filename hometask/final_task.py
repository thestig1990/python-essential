# Script developed to find the roots of quadratic equation
import sys
from math import *

# main() here our program will be started, and all required data asked
def main():
    print("Please, enter the coefficients of quadratic equation: ax^2+bx+c=0")


# ask_value(message?????) this function should ask user for input, and then 
# return variable. Good to have additional input validation here.
def ask_value(message=None):
    try:
        a, b, c = int(input("a = ")), int(input("b = ")), int(input("c = "))
    except:
        print("The type of coefficients must be an integer")
        sys.exit()
    else:
        if type(a) == int and type(b) == int and type(c) == int:
            return a, b, c



# discriminant(a,b,c) no much, no less just return discriminant.
def discriminant(a, b, c):
    D = b**2 - 4*a*c
    return D


# roots(D,a,b) will show on the screen all acceptable roots
def roots(D, a, b):
    if D >= 0:
        x1 = (-b - D**0.5) / (2*a)
        x2 = (-b + D**0.5) / (2*a)
    elif D < 0:
        print('No roots, D < 0')
        sys.exit()
    elif D == 0:
        x1 = -b/(2*a)
        x2 = -b/(2*a)
    if x1 >= x2:
        return round(x2, 5), round(x1, 5)
    else:
        return round(x1, 5), round(x2, 5)


# solv_square(a,b,c) this function should contain inside discriminant
# and roots functions.
def solv_square(a,b,c):
    D = discriminant(a, b, c)
    x1, x2 = roots(D, a, b)
    print("Discriminant: D =", D)
    print("Roots of the equation: ", "x1 = ", x1, "; ","x2 = ", x2, sep="")


# call the function 'main'
main()

# call the function 'ask_value' and record the result in to the variables a, b, c
a, b, c = ask_value()

# call the function 'solv_square'
solv_square(a, b, c)

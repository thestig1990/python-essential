import sys


# function declaration
def solve(a, b, c):
    D = b**2 - 4*a*c
    print('Discriminant D =', D)
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
        return x2, x1
    else:
        return x1, x2


# read the data
a, b, c = int(input()), int(input()), int(input())

# call the function and record the work result in the variable x1 and x2
x1, x2 = solve(a, b, c)

# printing roots of the equation
print("Roots of the equation: ", "x1 =", x1, "; ","x2 =", x2)


try:
  print(x)
except:
  print("An exception occurred")

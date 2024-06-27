import math

def is_number(n):
    try:
        float(n)
    except ValueError: return False
    return True

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def relu(x):
    if (x <= 0): return 0
    return x

def elu(x):
    if (x <= 0): return 0.01 * (math.exp(x) - 1)
    return x

# MAIN PROGRAM
x = input("Enter a number: ")
if is_number(x) == False:
    print("x must be a number")
    exit()

typeFunction = input("Input activation Function ( sigmoid | relu | elu ) : ")
if (typeFunction != "sigmoid") and (typeFunction != "relu") and (typeFunction != "elu"):
    print(typeFunction, "is not supported")
    exit()

x = float(x)
if typeFunction == "sigmoid": print(typeFunction, ": f(", x, ") =", sigmoid(x))
else: 
    if typeFunction == "relu": print(typeFunction, ": f(", x, ") =", relu(x))
    else: print(typeFunction, ": f(", x, ") =", elu(x))

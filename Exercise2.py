import math

def isNumber(n):
    try:
        float(n)
    except ValueError: return False
    return True

def Sigmoid(x):
    return 1 / (1 + math.exp(-x))

def Relu(x):
    if (x <= 0): return 0
    return x

def Elu(x):
    if (x <= 0): return 0.01 * (math.exp(x) - 1)
    return x

# MAIN PROGRAM
x = input("Enter a number: ")
if isNumber(x) == False:
    print("x must be a number")
    exit()

typeFunction = input("Input activation Function ( sigmoid | relu | elu ) : ")
if (typeFunction != "sigmoid") and (typeFunction != "relu") and (typeFunction != "elu"):
    print(typeFunction, "is not supported")
    exit()

x = float(x)
if typeFunction == "sigmoid": print(typeFunction, ": f(", x, ") =", Sigmoid(x))
else: 
    if typeFunction == "relu": print(typeFunction, ": f(", x, ") =", Relu(x))
    else: print(typeFunction, ": f(", x, ") =", Elu(x))

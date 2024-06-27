def calc_fact(n):
    res = 1
    for i in range(2, n + 1, 1):
        res *= i
    return res

def calc_sin(x, n):
    res = x
    for i in range(1, n + 1, 1):
        add = x**(2 * i + 1) / calc_fact(2 * i + 1)
        if i % 2 == 0:
            res += add
        else:
            res -= add
    return res

def calc_cos(x, n):
    res = 1
    for i in range(1, n + 1, 1):
        add = x**(2 * i) / calc_fact(2 * i)
        if i % 2 == 0:
            res += add
        else:
            res -= add
    return res

def calc_sinh(x, n):
    res = x
    for i in range(1, n + 1, 1):
        res += x**(2 * i + 1) / calc_fact(2 * i + 1)
    return res

def calc_cosh(x, n):
    res = 1
    for i in range(1, n + 1, 1):
        res += x**(2 * i) / calc_fact(2 * i)
    return res

x = float(input("Input an integer x: "))
n = int(input("Input times you want to repeat: "))

print(calc_sin(x, n))
print(calc_cos(x, n))
print(calc_sinh(x, n))
print(calc_cosh(x, n))
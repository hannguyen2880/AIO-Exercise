def md_nre_single_sample(y, y_hat, n, p):
    y_root = y**(1 / n)
    y_hat_root = y_hat**(1/ n)
    return (y_root - y_hat_root) ** p

y = float(input("Input value of y: "))
y_hat = float(input("Input value of y_hat: "))
n = int(input("Input value of n:  "))
p = int(input("Input value of p:  "))

print(md_nre_single_sample(y, y_hat, n, p))
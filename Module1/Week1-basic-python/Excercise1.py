def is_integer(n):
    return n == int(n)

# MAIN PROGRAM
tp = float(input("Enter tp: "))
if is_integer(tp) == 0:
    print("tp must be int")
    exit()

fp = float(input("Enter fp: "))
if is_integer(fp) == 0:
    print("fp must be int")
    exit()

fn = float(input("Enter fn: "))
if is_integer(fn) == 0:
    print("fn must be int")
    exit()

if (tp <= 0) or (fp <= 0) or (fn <= 0):
    print("tp and fp and fn must be greater than 0")
    exit()

#calculate
precision = tp / (tp + fp)
recall = tp / (tp + fn)
f1_score = 2 * (precision * recall) / (precision + recall)

#print result
print("Precision is", precision)
print("Recall is", recall)
print("F1-Score is", f1_score)
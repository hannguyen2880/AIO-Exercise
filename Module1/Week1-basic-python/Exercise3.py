import math
import random as rd

def calc_mae(target, predict):
    return abs(target - predict)

def calc_mse(target, predict):
    return (target - predict)**2

num_samples = input("Input number of samples ( integer number ) which are generated: ")
if num_samples.isnumeric() == False:
    print("Number of samples must be an integer number")
    exit()

loss_name = input("Input loss name: ")
num_samples = int(num_samples)
final_loss = 0

for sample in range(num_samples):
    predict = rd.uniform(0, 10)
    target = rd.uniform(0, 10)

    if loss_name == "MAE":
        loss = calc_mae(target, predict)
    else:
        loss = calc_mse(target, predict)

    final_loss += loss
    print("loss name: ", loss_name, ", sample: ", sample, ", predict: ", predict, ", target: ", target, ", loss: ", loss)

final_loss /= num_samples
print("final ", loss_name, ": ", final_loss)
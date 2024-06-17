def max_kernel(list, k):
    res = []
    sub_list = []
    for value in list:
        sub_list.append(value)
        if len(sub_list) == k:
            res.append(max(sub_list))
            del sub_list[0]
    return res

#MAIN PROGRAM
assert max_kernel ([3 , 4 , 5 , 1 , -44] , 3) == [5 , 5 , 5]
num_list = [3 , 4 , 5 , 1 , -44 , 5 ,10 , 12 ,33 , 1]
k = 3
print (max_kernel (num_list , k ))
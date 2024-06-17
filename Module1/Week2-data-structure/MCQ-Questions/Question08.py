def my_function(n) :
    if len(n) == 1:
        return n[0]
    min_value = n[0]
    for value in n:
        if min_value > value:
            min_value = value
        
    return min_value

my_list = [1, 22, 93, -100]
assert my_function(my_list) == -100

my_list = [1 , 2 , 3 , -1]
print (my_function(my_list))
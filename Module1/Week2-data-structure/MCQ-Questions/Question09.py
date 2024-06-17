def my_function(n) :
    if len(n) == 1:
        return n[0]
    max_value = n[0]
    for value in n:
        if max_value < value:
            max_value = value
        
    return max_value

my_list = [1001, 9, 100, 0]
assert my_function(my_list) == 1001

my_list = [1, 9, 9, 0]
print (my_function(my_list))
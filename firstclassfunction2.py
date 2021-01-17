# Use gitlab history to check the explaination 
# Parsing function as an argument into another function

def square(x):
    return x * x

# def cube(x):
#     return x * x * x

def my_map(func, arg_list): #Taken in a function as an argument and an array as argument
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

square = my_map(square, [1, 2, 3, 4, 5])

print square
#1 Required Arguments
def function_with_required(x, y):
    return(x + y)


print(function_with_required(1, 2))
#print(function_with_required(1))

#2 keyword arguments
def function_with_kw(first, second):
    print(f"{first} {second}")

print(function_with_kw(first="second", second="first"))

#3 default arguments
def function_with_default(x, y = 10):
    return(x * y)

print(function_with_default(10))
print(function_with_default(10, 15))

#4 variable arguments
def function_var_arguments(*args):
    total = 0
    for arg in args:
        total += float(arg)
    return total 

print(function_var_arguments(5, 4, 3))
print(function_var_arguments(100))
print(function_var_arguments(1, 2))

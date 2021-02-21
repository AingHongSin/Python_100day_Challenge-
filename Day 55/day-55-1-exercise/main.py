# Create the logging_decorator() function 👇

# def logging_decorator(function):
#     def wrapper_function(*args):
#         function(*args)
#         print(f"You called {function.__name__}{function()}\nIt Return: {sum(function())}")
#     return wrapper_function


# Use the decorator 👇

# def a_function():
#     return (1,2,3)

# call = logging_decorator(a_function)
# call()

#_______________________Solution_______________________

def logging_decorator(function):
    def wrapper_function(*args):
        print(f"You called {function.__name__}{args}")
        result = function(args[0], args[1], args[2])
        print(f"It Return: {result}")

    return wrapper_function

@logging_decorator
def a_function(a,b,c):
    return a * b * c

    
a_function(1,2,3)



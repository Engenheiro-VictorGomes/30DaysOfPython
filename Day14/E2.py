# 2. Explain the difference between higher order function, closure and decorator

# Higher-order functions
#   receive another function or returns a function as result

def isPositive(number):
    return number>0

numbers = [i for i in (-5,6)]
positiveNumbers = list(filter(isPositive, numbers))
                        #filter is a higher-order

# Closures:
#   Capture variables and keep this value
def counter():
    count = 0
    def inner():
        nonlocal count
        count += 1
        print(count)
    return inner

c = counter()
c() # Output: 1
c() # Output: 2
c() # Output: 3


# Decorators:
#   receives a function and returns a function, used to change the behavior of one function

# Example 01:
def myFunction():
    return "myFunction"
print(myFunction())
def decorator(func):
    def wrapper():
        result = 'Decorated:' + func()
        return result
    return wrapper
myDecoratedFunction = decorator(myFunction)
print(myDecoratedFunction())

#Example 02:
def decorator(func):
    def wrapper(*args, **kwargs):
        print("Before decorated function")
        result = func(*args, **kwargs)
        print("After decorated function")
        return result
    return wrapper

@decorator
def myFunction(a, b):
    return a + b

result = myFunction(1, 2)
print(result)


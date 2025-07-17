def add(a,b):
    result = a+b
    return result


def sub(a,b):
    c = a - b
    return c


def mul(a,b):
    c = a * b
    return c


def div(a,b):
    try:
      c = a / b
      return c
    except ZeroDivisionError:
      print("you cannot divide by zero:")






# import math_utlis as m 
# a = int(input("Enter your first number:"))
# b = int(input("Enter your second number:"))

# m.add(a,b)




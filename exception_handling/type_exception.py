num1 =10
num2 = 20

try:
    #its expecting the sting but got the int value so the exception raised
    print("sum of two numbers=" +num1+num2)
except TypeError:
    print("exception raised")

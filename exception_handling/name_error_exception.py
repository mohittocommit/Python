num1=10
num2=20

try:
    #tried to add num1 with num3, but num3 is not defined
    print("sum of two numbers=", num1+num3)
except NameError:
    print("exception raised")


#another part of the runs just fine
print("I got the exception concept")

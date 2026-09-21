import math

num = float(input("Give me a number: "))
num = num-math.floor(num)
if num==0:
    print("This number is an integer.")
else:
    print("This number is a decimal.")
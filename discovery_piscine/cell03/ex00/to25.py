num = int(input("Enter a number less than 25\n"))
if num > 25 :
    print("Error")
else:
    loop = 26-num
    for i in range(loop) :
        print("Inside the loop, my variable is "+str(num))
        num = num+1
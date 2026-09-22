import sys

num = len(sys.argv)-1
if num != 1:
    print("none")
else:
    par = str(input("What was the parameter? "))
    if par == sys.argv[1]:
        print("Good job!")
    else:
        print("Nope, sorry...")
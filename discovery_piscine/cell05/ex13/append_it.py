import sys

num = len(sys.argv)-1
if num == 0:
    print("none")
else:
    for i in range(num):
        if sys.argv[i+1].endswith("ism"):
            pass
        else:
            print(sys.argv[i+1]+"ism")
import sys

num = len(sys.argv)-1
if num < 2:
    print("none")
else:
    for i in range(num):
        print(sys.argv[num-i])
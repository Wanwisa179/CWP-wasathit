import sys

num = len(sys.argv)-1
if num != 1:
    print("none")
else:
    print(sys.argv[1].upper())
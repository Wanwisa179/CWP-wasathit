import sys

num = len(sys.argv)-1
if num == 0:
    print("none")
else:
    print("parameters: "+str(num))
    for i in range(num):
        print(str(sys.argv[i+1])+":"+str(len(sys.argv[i+1])))
import sys

num = len(sys.argv)-1
lst = sys.argv
if num != 2:
    print("none")
else:
    if int(lst[1]) <= int(lst[2]):
        new = int(lst[1])
        slt = [int(lst[1])]
        while new != int(lst[2]):
            new = new+1
            slt.append(new)
        print(slt)
    else:
        new = int(lst[1])
        slt = [int(lst[1])]
        while new != int(lst[2]):
            new = new-1
            slt.append(new)
        print(slt)
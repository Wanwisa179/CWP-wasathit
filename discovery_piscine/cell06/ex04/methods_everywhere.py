import sys

def shrink(word=None):
    print(str(word[:8]))

def enlarge(word=None):
    add = 8-len(word)
    new = word
    for i in range(add):
        new = str(new)+"z"
    print(new)

num = len(sys.argv)-1
if num == 0:
    print("none")
else:
    for i in range(num):
        if len(sys.argv[i+1]) > 8:
            shrink(str(sys.argv[i+1]))
        elif len(sys.argv[i+1]) < 8:
            enlarge(str((sys.argv[i+1])))
        else:
            print(sys.argv[i+1])
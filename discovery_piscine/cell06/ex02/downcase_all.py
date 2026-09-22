import sys

def downcase_it(word):
    print(word.lower())

num = len(sys.argv)-1
if num == 0:
    print("none")
else:
    for i in range(num):
        downcase_it(str(sys.argv[i+1]))
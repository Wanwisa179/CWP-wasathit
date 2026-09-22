import sys
import re

num = len(sys.argv)-1
if num == 0:
    print("none")
else:
    for i in range((len(re.findall("z", sys.argv[1])))):
        print("z", end="")
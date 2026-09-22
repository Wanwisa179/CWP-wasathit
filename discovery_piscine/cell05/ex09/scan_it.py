import sys
import re

num = len(sys.argv)-1
if num != 2:
    print("none")
else:
    ans = re.findall(sys.argv[1], sys.argv[2])
    print(len(ans))
ori =  [2, 8, 9, 48, 8, 22,-12, 2]
new = []
for i in range(len(ori)):
    if int(ori[i]) > 5:
        new.append(ori[i]+2)
print(ori)
print(new)
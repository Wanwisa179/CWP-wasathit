ori =  [2, 8, 9, 48, 8, 22,-12, 2]
new = []
for i in range(len(ori)):
    if int(ori[i]) > 5:
        for j in range(len(new)):
            if new[j] == ori[i]+2:
                break
            elif j == len(new)-1:
                new.append(ori[i]+2)
        if new == []:
            new.append(ori[i]+2)
print(ori)
print(new)
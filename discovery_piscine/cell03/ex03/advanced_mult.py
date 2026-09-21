loop = 0
roop = 0
while loop < 11:
    print("Table de "+str(loop)+": ", end="")
    while roop < 11:
        if(roop == 10):
            print(str(loop*roop)+" ")
        else:
            print(str(loop*roop)+" ", end="")
        roop = roop+1
    roop = 0
    loop = loop+1
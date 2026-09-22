import sys
loop = 0
roop = 0

if len(sys.argv) > 1:
    print("none")
else:
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
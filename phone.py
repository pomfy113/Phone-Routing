# !python
from pathlib import Path
from time import time

routefile = open("route-costs-106000.txt").read().split("\n")
phonenum = "+861721532"
print("Looking for", phonenum)

maxmatch = 0
closestmatch = None
perfectmatch = False
starttime = time()

for i in range(len(routefile)-1):
    if perfectmatch is True:
        break
    if routefile[i][1] == phonenum[1]:
        currentmatch = 1
        for j in range(len(phonenum)-1):
            if routefile[i][j+1] == phonenum[j+1]:
                currentmatch += 1
                if currentmatch == len(phonenum):
                    closestmatch = routefile[i]
                    perfectmatch = True
            elif currentmatch > maxmatch:
                closestmatch = routefile[i]
            else:
                break

print(closestmatch, phonenum)
print("Cost:", "$"+closestmatch.split(",")[1])
print(time() - starttime)

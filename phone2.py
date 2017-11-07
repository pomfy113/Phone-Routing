"""Scenario 2."""
from pathlib import Path

pregen_routes = Path("pregen_routes.txt")
if pregen_routes.is_file():
    print("Pregen detected.")
    routes = open(pregen_routes).read().split("\n")
else:
    filename = "route-costs-106000.txt"
    routes = sorted(open(filename).read().split("\n"))
    histofile = open("pregen_routes.txt", "w+")
    histofile.write("\n".join(routes))
    histofile.close()

# phonenum = open("phone-numbers-10.txt").read().split("\n")
# phonenum_list = open('phone-numbers-10.txt').read().split("\n")
phonenum_list = ['+1573533', '+44931708', '+1201895']
# phonenum_list = ['+44931708']

# routes = ["+1201,0.07", "+120,0.05", "+12071,0.05", '+15,0.05', '+449317089,0.05', '+449317953,0.07']
maxmatch = 1
closestmatch = None
perfectmatch = False

matches = []
phonenumberstuff = []
# Let's try a binary search?
for phonenum in phonenum_list:
    closestmatch = None
    perfectmatch = False
    maxmatch = 2
    if phonenum is "":
        print("END")
        break

    for i in range(len(routes)):
        if perfectmatch is True:
            break
        elif routes[i] == "":
            continue
        elif routes[i][1] == phonenum[1]:
            currentmatch = 1
            for j in range(len(phonenum)-1):
                if routes[i][j+1] == phonenum[j+1]:
                    # print("Still inside!", j, routes[i], phonenum)
                    currentmatch += 1
                    if routes[i][j+2] == ",":
                        if currentmatch > maxmatch:
                            closestmatch = routes[i]
                            maxmatch = currentmatch
                            break
                        else:
                            break
                else:
                    break
    if closestmatch is not None:
        matches.append("$"+closestmatch.split(',')[1])
        phonenumberstuff.append(closestmatch.split(',')[0])
    else:
        matches.append(" N/A ")
        phonenumberstuff.append("???")

print(matches)
for i in range(len(phonenum_list)):
    print(matches[i], phonenumberstuff[i], "-", phonenum_list[i])
# print("Cost:", "$"+closestmatch.split(",")[1])
# print(time() - starttime)


# print(time() - starttime)

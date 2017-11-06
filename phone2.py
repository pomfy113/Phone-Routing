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
phonenum = ["+1256"]
print("Looking for", phonenum)

maxmatch = 0
closestmatch = None
perfectmatch = False
# Let's try a binary search?
for number in phonenum:
    perfectmatch = False
    left = 0
    right = len(routes)-1

    # Let's cut it a bit.
    for j in range(3):
        # Index for the middle element
        middle = (left + right) // 2
        middle_item = routes[middle]
        # If it's the middle, return that
        if number > middle_item:
            left = middle+1
            print(left, routes[left])
        elif number < middle_item:
            right = middle-1
            print(right, routes[right])
    print(left, right)
    # Let's change to the linear search
    while left < right:
        print(left, routes[left], right, routes[right])
        print(routes[left], "blabla", number[1])
        if perfectmatch is True:
            break
        if routes[left][1] == number[1]:
            currentmatch = 1
            for j in range(len(number)-1):
                if routes[left][j+1] == number[j+1]:
                    currentmatch += 1
                    if currentmatch == len(number):
                        print(closestmatch, "is a perfect match")
                        closestmatch = routes[left]
                        perfectmatch = True
                elif currentmatch > maxmatch:
                    closestmatch = routes[left]
                else:
                    break
        left += 1


print(closestmatch, phonenum)
# print(time() - starttime)

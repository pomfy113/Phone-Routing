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
    left = 0
    right = len(routes)-1

    while True:
        # Index for the middle element
        middle = (left + right) // 2
        middle_item = routes[middle]
        # If it's the middle, return that
        if right < left:
            print(routes[left])
            break
        elif number > middle_item:
            left = middle+1
        elif number < middle_item:
            right = middle-1


# print(closestmatch, phonenum)
# print(time() - starttime)

# ===== DILYAZ STYLE =====

import math

# Part 1: hypotenuse of two right triangles
def dhypotenuse(da, db):
    return math.sqrt(da * da + db * db)

da1, db1 = map(float, input().split())
da2, db2 = map(float, input().split())

dh1 = dhypotenuse(da1, db1)
dh2 = dhypotenuse(da2, db2)

if dh1 > dh2:
    print("First hypotenuse is greater")
elif dh1 < dh2:
    print("Second hypotenuse is greater")
else:
    print("Hypotenuses are equal")

# Part 2: sort letters in each word alphabetically
dtext = input().split()
dresult = []

for dword in dtext:
    dresult.append("".join(sorted(dword)))

print(" ".join(dresult))

# ===== DILYAZ STYLE =====

# Part 1: Divide fractions and reduce 
def dgcd(da, db):
    while db != 0:
        da, db = db, da % db
    return da

dA = int(input())
dB = int(input())
dC = int(input())
dD = int(input())

dnum = dA * dD
dden = dB * dC

dg = dgcd(dnum, dden)

dnum //= dg
dden //= dg

print(dnum, dden)

# Part 2: Points inside a circle 
def dinside_circle(dx, dy, dr, px, py):
    return (px - dx) ** 2 + (py - dy) ** 2 < dr ** 2

dx = float(input())
dy = float(input())
dr = float(input())

dcount = 0

for i in range(3):
    dpx = float(input())
    dpy = float(input())
    if dinside_circle(dx, dy, dr, dpx, dpy):
        dcount += 1

print(dcount)

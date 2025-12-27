# ===== DILYAZ STYLE =====
import math

# Part 1: GCD and LCM 

def dgcd(da, db):
    while db != 0:
        da, db = db, da % db
    return da

da = int(input())
db = int(input())

dg = dgcd(da, db)
dlcm = (da * db) // dg

print("GCD:", dg)
print("LCM:", dlcm)

# Part 2: Area of a convex quadrilateral 

da = float(input())
db = float(input())
dc = float(input())
dd = float(input())
ddiag = float(input())

ds1 = (da + db + ddiag) / 2
darea1 = math.sqrt(ds1 * (ds1 - da) * (ds1 - db) * (ds1 - ddiag))

ds2 = (dc + dd + ddiag) / 2
darea2 = math.sqrt(ds2 * (ds2 - dc) * (ds2 - dd) * (ds2 - ddiag))

darea = darea1 + darea2
print("Area:", darea)

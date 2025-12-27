# ===== DILYAZ STYLE =====

# Part 1: Subtract fractions A/B - C/D 

def dgcd(dx, dy):
    while dy != 0:
        dx, dy = dy, dx % dy
    return dx

dA, dB = map(int, input().split())
dC, dD = map(int, input().split())

dnum = dA * dD - dC * dB
dden = dB * dD

dg = dgcd(abs(dnum), dden)

dnum //= dg
dden //= dg

print(dnum, dden)

# Part 2: Print all divisors of a number 

dn = int(input())

for di in range(1, dn + 1):
    if dn % di == 0:
        print(di, end=" ")

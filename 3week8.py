# ===== DILYAZ STYLE =====

# Part 1
dn = int(input())

dresult = []
for dnum in range(1, dn + 1):
    dtemp = dnum
    dok = True
    while dtemp > 0:
        ddigit = dtemp % 10
        if ddigit == 0 or dnum % ddigit != 0:
            dok = False
            break
        dtemp //= 10
    if dok:
        dresult.append(dnum)

print(" ".join(map(str, dresult)))

# Part 2
dm = int(input())
darray = list(map(int, input().split()))

doriginal = darray.copy()

darray[0], darray[-1] = darray[-1], darray[0]

print("Original:", *doriginal)
print("Result:", *darray)

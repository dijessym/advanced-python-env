# ===== DILYAZ STYLE =====

# Task 1: Area of geometric shapes 

dshape = input()

if dshape == "rectangle":
    da = float(input())
    db = float(input())
    darea = da * db
    print(darea)

elif dshape == "square":
    da = float(input())
    darea = da * da
    print(darea)

elif dshape == "circle":
    dr = float(input())
    darea = 3.14 * dr * dr
    print(darea)

# Task 2: Arrays sum and average 

for i in range(3):
    darr = list(map(int, input().split()))
    dsum = sum(darr)
    davg = dsum / len(darr)
    print(dsum, davg)

# ===== DILYAZ STYLE =====

# Task 2.1 
# Area of a regular hexagon using triangle area

da = float(input())
dtriangle_area = (3 ** 0.5) / 4 * da * da
dhexagon_area = 6 * dtriangle_area
print(dhexagon_area)

# Task 2.2 
# Areas of three rectangles

for i in range(3):
    da = float(input())
    db = float(input())
    darea = da * db
    print(darea)

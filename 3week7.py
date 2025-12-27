# ===== DILYAZ STYLE =====
import math

def drectangle_area(dx, dy):
    return dx * dy

def dright_triangle_area(da, db):
    return da * db / 2

dx = float(input())
dy = float(input())
dz = float(input())
dt = float(input())

drect = drectangle_area(dx, dy)
dtri = dright_triangle_area(dz, dt)

darea = drect + dtri
print("Area:", darea)

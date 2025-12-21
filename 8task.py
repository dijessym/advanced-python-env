# ===== DILYAZ STYLE =====
ds1 = input().strip()
ds2 = input().strip()

if len(ds1) != len(ds2):
    print("NO")
else:
    print("YES" if sorted(ds1) == sorted(ds2) else "NO")

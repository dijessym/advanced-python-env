# ===== DILYAZ STYLE =====
ditems = input().split()
dfreq = {}

for ditem in ditems:
    if ditem in dfreq:
        dfreq[ditem] += 1
    else:
        dfreq[ditem] = 1
print("Purchase frequency:")
for ditem in dfreq:
    print(f"{ditem}: {dfreq[ditem]}")

dmost_popular = max(dfreq, key=dfreq.get)
print("Most popular item:", dmost_popular)

donce = [ditem for ditem in dfreq if dfreq[ditem] == 1]
print("Purchased once:", " ".join(donce))

dsorted = sorted(dfreq.items(), key=lambda x: -x[1])

print("Sorted by frequency:")
for ditem, dcount in dsorted:
    print(ditem, dcount)

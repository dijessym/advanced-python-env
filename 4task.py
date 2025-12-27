# ===== DILYAZ STYLE =====
dline = input().split()
dn = int(dline[0])
dm = int(dline[1])

dtext = input()
dwords = set()
for i in range(dn - dm + 1):
    dword = dtext[i:i+dm]
    dwords.add(dword)

dcount = len(dwords)

print(dcount)
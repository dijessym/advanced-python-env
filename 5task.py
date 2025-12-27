# ===== DILYAZ STYLE =====
dletters = set("ABCEHKMOPTXY")
dn = int(input())

for i in range(dn):
    dplate = input().strip()
    
    if len(dplate) != 6:
        print("No")
        continue
    
    dfirst = dplate[0]        
    dmiddle = dplate[1:4]    
    dlast = dplate[4:6]      
    
    if not dmiddle.isdigit():
        print("No")
        continue
    
    if not (dfirst in dletters and
            dlast[0] in dletters and
            dlast[1] in dletters):
        print("No")
        continue
    
    print("Yes")

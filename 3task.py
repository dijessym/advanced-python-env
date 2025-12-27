# ===== DILYAZ STYLE =====
dequation = input()

dfirst = dequation[0]    
dsign = dequation[1]    
dthird = dequation[2]   
dequals = dequation[3]  
dfifth = dequation[4]   

if dfirst == 'x':
    dnum1 = int(dthird)
    dnum2 = int(dfifth)
    
    if dsign == '+':
        dresult = dnum2 - dnum1
    else:  
        dresult = dnum2 + dnum1
        
elif dthird == 'x':
    dnum1 = int(dfirst)
    dnum2 = int(dfifth)
    
    if dsign == '+':
        dresult = dnum2 - dnum1
    else:  
        dresult = dnum1 - dnum2
        
else: 
    dnum1 = int(dfirst)
    dnum2 = int(dthird)
    
    if dsign == '+':
        dresult = dnum1 + dnum2
    else:  
        dresult = dnum1 - dnum2

print(dresult)
# ===== DILYAZ STYLE =====
def all_eq(dlist):
    dmax_len = max(len(dstr) for dstr in dlist)
    dresult = []
    
    for dstr in dlist:
        dresult.append(dstr + "_" * (dmax_len - len(dstr)))
    
    return dresult

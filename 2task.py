a = input()
b = input()

len_b = len(b)
count = 0

shifts = []
for i in range(len_b):
    shift = b[i:] + b[:i]
    shifts.append(shift)
for i in range(len(a) - len_b + 1):
    substring = a[i:i + len_b]
    
    if substring in shifts:
        count += 1

print(count)
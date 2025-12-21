d = input("Введите строку: ")
count = 0

for i in range(len(d) - 4):
    if d[i] == '>' and d[i+1] == '>' and d[i+2] == '-' and d[i+3] == '-' and d[i+4] == '>':
        count += 1
    elif d[i] == '<' and d[i+1] == '-' and d<<[i+2] == '-' and d[i+3] == '<' and d[i+4] == '<':
        count += 1

print(count)
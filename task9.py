ticket = input("Enter ticket number: ")

if sum(int(digit) for digit in ticket[:3]) == sum(int(digit) for digit in ticket[3:]):
    print("YES")
else:
    print("NO")
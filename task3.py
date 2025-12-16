A = float(input())

integer_part = int(A)
fractional_part = int(round((A - integer_part) * 100))

result = fractional_part + integer_part / 100
print(result)

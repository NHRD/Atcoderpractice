n = input()

sum = 0

for c in n:
    sum = sum + int(c)

if sum % 9 == 0:
    print("Yes")
else:
    print("No")
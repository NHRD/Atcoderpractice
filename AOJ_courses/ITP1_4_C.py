cal = []
cals = []

while True:
    cal =list(map(str, input().split()))
    if cal[1] == "?":
        break
    cals.append(cal)

for i in range(len(cals)):
    cal = cals[i]
    a = int(cals[i][0])
    b = int(cals[i][2])
    op = cals[i][1]
    if op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        print(a // b)


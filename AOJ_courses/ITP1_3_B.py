num = 0
cases = []
a = 0

while True:
    a = int(input())
    if a == 0:
        break
    cases.append(a)
    a = 0

for i in range(len(cases)):
    print("Case {}: {}" .format(i + 1, cases[i]))
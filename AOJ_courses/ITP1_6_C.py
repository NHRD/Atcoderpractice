n = int(input())
i = 0
hins = []
while i < n:
    hin = list(map(int, input().split()))
    hins.append(hin)
    i += 1

a = [[0 for i in range(10)] for i in range(3)]
b = [[0 for i in range(10)] for i in range(3)]
c = [[0 for i in range(10)] for i in range(3)]
d = [[0 for i in range(10)] for i in range(3)]

for i in range(n):
    hin = hins[i]
    #print(hin)
    tou = str(hin[0] - 1)
    kai = hin[1] - 1
    hey = hin[2] - 1
    nin = hin[3]
    #print(tou, kai, hey, nin)

    if tou == "0":
        a[kai][hey] = a[kai][hey] + nin
    elif tou == "1":
        b[kai][hey] = b[kai][hey] + nin
    elif tou == "2":
        c[kai][hey] = c[kai][hey] + nin
    elif tou == "3":
        d[kai][hey] = d[kai][hey] + nin
aida = "#" * 20

for i in range(3):
    for j in range(10):
        if j == 9:
            print(" {}" .format(a[i][j]))
        else:
            print(" {}" .format(a[i][j]), end="")
print(aida)
for i in range(3):
    for j in range(10):
        if j == 9:
            print(" {}" .format(b[i][j]))
        else:
            print(" {}" .format(b[i][j]), end="")
print(aida)
for i in range(3):
    for j in range(10):
        if j == 9:
            print(" {}" .format(c[i][j]))
        else:
            print(" {}" .format(c[i][j]), end="")
print(aida)
for i in range(3):
    for j in range(10):
        if j == 9:
            print(" {}" .format(d[i][j]))
        else:
            print(" {}" .format(d[i][j]), end="")
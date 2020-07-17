abc = list(map(int, input().split()))

x1 = abc[0]
y1 = abc[1]

for i in range(len(abc)):
    if i % 2 == 0:
        abc[i] = abc[i] - x1
    else:
        abc[i] = abc[i] - y1

print(abs(abc[2] * abc[5] - abc[3] * abc[4])/2)
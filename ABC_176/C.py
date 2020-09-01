n = int(input())
a = list(map(int, input().split()))
dif  = 0
sum = 0

for i in range(len(a) - 1):
    dif = a[i] - a[i+1]
    if dif > 0:
        sum = sum + dif
        a[i + 1] = a[i + 1] + dif

print(sum)

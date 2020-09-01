n = int(input())
a = list(map(int, input().split()))

comb = len(a) * (len(a) - 1) / 2
comb = int(comb)

sum = 0

for i in range(comb):
    #print(a)
    for i in range(1, len(a)):
        #print(a[i])
        sum = sum + a[0] * a[i]
    a = a[1:]
    #print(a)

print(sum % (10**9 + 7))
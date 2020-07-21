n, m = map(int, input().split())
a = []
b = []
result = []
sum = 0

for i in range(n):
   mat = list(map(int, input().split()))
   a.append(mat)
   mat = []

for j in range(m):
    b.append(int(input()))

#print(a)
#print(b)

for k in range(n):
    for l in range(m):
        sum += a[k][l] * b[l]
    result.append(sum)
    sum = 0

for i in range(len(result)):
    print(result[i])
k = int(input())
if k % 7 == 0:
    L = 9 * k / 7
else:
    L = 9 * k
 
if L % 2 == 0 or L % 5 == 0:
    print(-1)

m = 10

for i in range(k):
    m = m % L
    if m == 1:
        print(i + 1)
        exit()
    else:
        m = m * 10
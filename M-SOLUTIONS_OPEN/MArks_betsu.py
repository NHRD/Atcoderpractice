n, k = map(int, input().split())
scs = list(map(int, input().split()))

for i in range(k, n):
    if  scs[i] > scs[i - k]:
        print("Yes")
    else:
        print("No")
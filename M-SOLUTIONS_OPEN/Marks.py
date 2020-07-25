n, k = map(int, input().split())
scs = list(map(int, input().split()))
#print(scs)
#res = []
re = 1
pre = 0

for i in range(n - k + 1):
    for j in range(k):
        re = re * scs[i + j]
    if pre < re and i != 0:
        print("Yes")
    elif i != 0:
        print("No")
    pre = re
    re = 1

"""
for i in range(1, n - k + 1):
    if res[i - 1] < res [i]:
        print("Yes")
    else:
        print("No")
"""
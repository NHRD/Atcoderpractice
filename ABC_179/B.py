import sys

n = int(input())

zoro = 0
res = 0

for i in range(n):
    d1, d2 = map(int, input().split())

    if d1 != d2:
        zoro = 0
    else:
        zoro = zoro + 1
    if zoro == 3:
        res = 1

if res == 1:
    print("Yes")
else:
    print("No")

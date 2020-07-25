a, b, c = map(int, input().split())
k = int(input())

for i in range(k):
    if a < b and b < c:
        print("Yes")
        exit()
    elif a >= b:
        b = b * 2
    elif b >= c:
        c = c * 2

if a < b and b < c:
    print("Yes")
else:
    print("No")

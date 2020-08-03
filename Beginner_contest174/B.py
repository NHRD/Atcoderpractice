n, d = map(int, input().split())

result = 0

for i in range(n):
    x, y = map(int, input().split())
    if (x ** 2 + y ** 2) ** (1/2) <= d:
        result += 1

print(result)



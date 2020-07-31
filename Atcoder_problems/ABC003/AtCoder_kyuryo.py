n = int(input())

sum = 0

for i in range(1, n+1):
    sum = sum + i

result = 10000 * sum / n
print(result)
print("close")
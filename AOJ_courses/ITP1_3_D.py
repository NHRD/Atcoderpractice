a, b, c = map(int, input().split())
divs = 0

for i in range(a, b+1):
    if c % i == 0:
        divs += 1

print(divs)
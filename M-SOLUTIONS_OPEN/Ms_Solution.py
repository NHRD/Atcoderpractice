import itertools

n = int(input())
points = []

for i in range(n):
    point = list(map(int, input().split()))
    points.append(point)
    if i == n - 1:
        break

def x_dir(x, p, n):
    lines = [i for i in range(1, n + 1]
    for i in range(1, n + 1):
        for v in itertools.combinations(lines, i):
        

def y_dir(y, p, n):

print(points)
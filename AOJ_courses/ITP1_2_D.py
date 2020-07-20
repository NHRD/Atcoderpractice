w, h, x, y, r = map(int, input().split())

x_min = x - r
x_max = x + r
y_min = y - r
y_max = y + r

if x_min >= 0 and x_max <= w:
    if y_min >= 0 and y_max <= h:
        print("Yes")
        exit()
print("No")

i = 3
while i > 0:
    print("Hello world")
    i = i - 1
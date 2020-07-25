import math
a, b, c = map(float, input().split())
c = math.radians(c)

s = (1 / 2) * a * b * math.sin(c)
l = a + b + (a ** 2 + b ** 2 - 2 * a * b * math.cos(c)) ** (1 / 2)
h = b * math.sin(c)

print(s)
print(l)
print(h)
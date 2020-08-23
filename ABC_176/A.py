n, x, t = map(int, input().split())

ama = n % x
fun = n // x

if ama != 0:
    print((fun+ 1) * t)

else:
    print(fun * t)
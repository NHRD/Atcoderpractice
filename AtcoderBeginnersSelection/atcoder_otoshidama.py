n, y = map(int, input().split())
flag = 0

for i in range(n + 1):
    for j in range(n - i + 1):
        if i*5000 + j *10000 + (n-i-j)*1000 == y:
            print("{} {} {}" .format(j, i, n-i-j))
            exit()
                
print("-1 -1 -1")
   
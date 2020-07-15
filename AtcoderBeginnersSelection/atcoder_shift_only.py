n = input()
a = input().split()
a = [int(s) for s in a]
div = 0

while  all(i % 2 ==0 for i in a):
    a = [i/2 for i in a]
    div += 1

print(div)
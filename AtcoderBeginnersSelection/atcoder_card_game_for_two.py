n = int(input())
a = list(map(int, input().split()))
a = sorted(a)
#print(a)
alice = 0
bob = 0

for i in range(len(a)):
    if i % 2 == 0:
        alice = alice + a.pop(-1)
    else:
        bob = bob + a.pop(-1)

print(alice - bob)
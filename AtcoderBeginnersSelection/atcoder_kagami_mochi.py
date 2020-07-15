n = int(input())
mochi = []
for i in range(n):
    mochi.append(input())

mochi_uni = list(set(mochi))
print(len(mochi_uni))
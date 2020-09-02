from statistics import mode

n, m = map(int, input().split())

rels = [i for i in range(n)]
inf = []
count = [0] * n

for i in range(m):
    rel = list(map(int, input().split()))
    rel = sorted(rel)
    inf.append(rel)

inf = sorted(inf)

for rel in inf:
    a = rel[0] - 1
    b = rel[1] - 1
    rels[b] = rels[a]

"""
for rel in rels:
    count[rel - 1] = count[rel - 1] + 1

res = rels.count(mode(rels))

while res < sum(count) - res:
    res = res + 1
    """

print(rels.count(mode(rels)))
from statistics import mode

n, m = map(int, input().split())

rels = [i for i in range(n + 1)]

for i in range(m):
    rel = list(map(int, input().split()))
    rel = sorted(rel)
    a = rel[0]
    b = rel[1]
    rels[b] = rels[a]
    
print(rels.count(mode(rels)))
n, m = map(int, input().split())

def exception(m):
    if m == 0:
        print("1")
        exit()

def relations(m):
    rels = []
    i = m
    while i < m:
        rel = list(map(int, input().split()))
        rels.append(rel)
        rel = []
        i = i - 1
    rels = sorted(rels)
    return rels

def factions(n):
    mb = 2 ** n - 1
    facm = []
    facms = []
    facb = ""
    for i in range(mb):
        bi = str(bin(i + 1))[2:]
        facb = "0" * (n - int(len(bi))) + bi 
        print(facb)
        for j in range(len(facb)):
            if facb[len(facb) - j - 1] == "1":
                facm.append(j + 1)
        if facm not in facms:
            facms.append(facm)
        facm = []
        facb = ""
        #facms = sorted(facms)
    return facms

def judge(rels, facms):

    return result

print(exception(m))
print(relations(m))
result = factions(n)
print(result)
print(len(result))
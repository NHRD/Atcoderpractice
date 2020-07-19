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
        #print(facb)
        for j in range(len(facb)):
            if facb[len(facb) - j - 1] == "1":
                facm.append(j + 1)
        if facm not in facms and len(facm) > 1:
            facms.append(facm)
        facm = []
        facb = ""
        #facms = sorted(facms)
    return facms

def testl(facms):
    print(facms)
    for i in range(len(facms)):
        print(facms[i])
        fac = facms[i]
        mb = 2 ** len(fac) - 1
        facm = []
        facms = []
        sum = 0
        for j in range(mb):
            bi = str(bin(j + 1))[2:]
            facb = "0" * (len(fac) - len(bi)) + bi
            for k in range(len(facb)):
                if bi[k] == "1" and sum < 2:
                    facm.append(fac[k])
                    sum += 1
                facms.append(facm)
                facm = []
            facb = ""
    return facms

def judge(rels, facms):
    for i in range(len(facms)):
        if facms[i] == rels:
            print(len(facms[i]))
            exit()

result = factions(n)
#result2 = testl(result)
print(result)
#print(result2)

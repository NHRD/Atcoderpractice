n, m = map(int, input().split())

def exception(m):
    if m == 0:
        print("1")
        exit()

def relations(m):
    rels = []
    for i in range(m):
        rel = list(map(int, input().split()))
        rels.append(rel)
        rel = []
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

def testl(facin):
    #print(facms)
    for i in range(len(facin)):
        #print(facms[i])
        fac = facin[i]
        mb = 2 ** len(fac) - 1
        facm = []
        facms = []
        sum = 0
        for j in range(mb):
            bi = str(bin(j + 1))[2:]
            facb = "0" * (len(fac) - len(bi)) + bi
            #print(facb)
            #print(len(facb))
            for k in range(len(facb)):
                #print(k)
                if facb[k] == "1" and sum < 2:
                    #print(fac[k])
                    facm.append(fac[k])
                    sum += 1
            if facm not in facms and len(facm) > 1:
                facms.append(facm)
            sum = 0
            facm = []
            facb = ""
    facms = sorted(facms)
    return facms

def judge(rels, facms):
    #print(rels)
    #print(facms)
    if facms == rels:
        print(len(facms))
        exit()

#result = factions(n)
#result2 = testl(result)
#print(result)
#print(result2)
#print(testl([[1,2], [1,2,3]]))

print("n = {}, m = {}" .format(n,m))
rels = relations(m)
exception(m)
fac = factions(n)
facms = testl(fac)
print(facms)
judge(rels, facms)
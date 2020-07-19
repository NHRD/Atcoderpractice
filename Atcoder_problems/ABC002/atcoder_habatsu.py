n, m = map(int, input().split())

if m == 0:
    print("1")
    exit()

rels = []
combs =[]

for i in range(m):
    rel = list(map(int, input().split()))
    rels.append(rel)
    rel = []

rels = sorted(rels)
#print(rels)


#print(mb)
pos = []
res = 0
prep = []

for k in range(n):
    mb = 2 ** (k + 1) - 1
    poss = []
    for i in range(mb):
        bins = bin(i)[2:]
        #print(bins)
        sums = 0
        for j in range(len(bins)):
            sums = sums + int(bins[j])
            #print(sums)
        if sums == 2:
            bins = "0" * (m - len(bins)) + bins
            #print(bins)
            for i in range(len(bins)):
                if bins[i] == "1":
                    pos.append(i+1)
            poss.append(pos)
            pos = []
        else:
            continue
        print(poss)
    for l in range(len(poss)):
        print(poss)
        if poss != rels:
            #print(poss[l])
            print(len(poss))
            exit()
        else:
            prep = poss
            print(prep)
        
#print(poss)
n, a, b = map(int, input().split())
nl = list(range(1, n + 1, 1))
#print(nl)
sumo = 0
sum = 0

for i in range(0, n):
    ns = str(nl[i])
    #print(ns)
    for j in range(len(ns)):
        sumo = sumo + int(ns[j])
    if sumo >= a and sumo <= b:
        sum = sum + int(ns)
    sumo = 0

print(sum)
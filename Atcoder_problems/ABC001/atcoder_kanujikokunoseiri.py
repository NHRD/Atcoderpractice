n = int(input())
s2e = []
s2es = []

for i in range(n):
    s, e = map(str, input().split("-"))

    if int(s[-1]) - 5 <= -1:
        s = s[:-1] + "0"
    else:
        s = s[:-1] + "5" 

    if  int(e[-1]) == 0:
        e = e[:-1] + "0"
    elif int(e[-1]) - 5 <= -1:
        e = e[:-1] + "5"
    else:
        if int(e[-2]) == 5:
            e = str(int(e[:-2]) + 1) + "00"
        else:
            e = e[:-2] + str(int(e[-2]) + 1) + "0"
        
    s2e.append(s)
    s2e.append(e)
    s2es.append(s2e)
    s2e = []

s2es = sorted(s2es)

for i in range(len(s2es)-1):
    if s2es[i][1] < s2es[i+1][0]:
        print("{}-{}" .format(str(s2es[i][0]), str(s2es[i][1])))

    elif s2es[i][1] >= s2es[i+1][0] and s2es[i][1] <= s2es[i+1][1]:
        s2es[i+1][0] = s2es[i][0]
    
    elif s2es[i][0] <= s2es[i+1][0] and s2es[i][1] >= s2es[i+1][1]:
        s2es[i+1][0] = s2es[i][0]
        s2es[i+1][1] = s2es[i][1]

print("{}-{}" .format(str(s2es[len(s2es)-1][0]), str(s2es[len(s2es)-1][1])))

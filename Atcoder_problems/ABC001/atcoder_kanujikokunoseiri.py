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
        e = e[:-2] + str(e[-2] + 1) + "0"
        
    s2e.append(s)
    s2e.append(e)
    s2es.append(s2e)
    s2e = []

s2es = sorted(s2es)
print(s2es)

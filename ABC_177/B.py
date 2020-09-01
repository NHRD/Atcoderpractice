s = input()
t = input()

mat = 0
res = 1000

ls = len(s)
lt = len(t)
#print(ls, lt)

di = ls - lt

for i in range(di + 1):
    tag = s[i:i + lt]
    #print(tag)
    #print(t)
    for j in range(lt):
        if t[j] != tag[j]:
            mat += 1
    if mat <= res:
        res = mat
    #print(res)
    mat = 0

print(res)




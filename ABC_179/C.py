n = int(input())

res = 0
c = 1

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append(cnt + 1)
        if temp!=1:
            arr.append(2)

        if arr==[]:
            arr.append(2)

    return arr

for i in range(1, n):
    #print(i)
    resu = factorization(i)
    #print(resu)
    if resu != []:
        for fac in resu:
            c = c * fac
        res = res + c
    c = 0

res = res + n - 1

print(res)

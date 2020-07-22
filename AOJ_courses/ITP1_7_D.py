n, m, l = map(int, input().split())

def acq_ab(n):
    a = []
    for i in range(n):
        if i == n:
            break
        ai = list(map(int, input().split()))
        a.append(ai)
    return a

def calc(a, b, n, m, l):
    ans = 0
    for i in range(n):
        for j in range(m):
            for k in range(l):
                ans = ans + a[] * b[]

#a = acq_ab(n)
#print(a)
#b = acq_ab(m)
#print(b)
calc([[1, 2], [0, 3], [4, 5]], [[1, 2, 1], [0, 3, 2]], 3, 2)
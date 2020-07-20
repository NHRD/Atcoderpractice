
"""def check_num(i, n):
    x = i
    if x % 3 == 0:
        print(" {}" .format(x), end="")
        end_check_num(x, n)
    incldue3(x, n)

def incldue3(i, n):
    x = i
    if x % 10 == 3:
        print(" {}" .format(x), end="")
        end_check_num(x, n)
    x = x //= 10
    if x != 0:
        incldue3(x, n)
    else:
        end_check_num(x, n)

def end_check_num(i , n):
    i = i + 1
    if i <= n:
        check_num(i, n)
    else:
        print("")

"""
N = int(input())
x = 0

for i in range(1,N+1):

    if i%3 == 0:
            print(" %d"%i,end = "");
    else:
        x = i
        while (x):
            if x%10 == 3:
                print(" %d"%i,end = "")
                break
            x //= 10
print()
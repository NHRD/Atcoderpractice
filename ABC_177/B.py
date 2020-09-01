s = input()
t = input()

res = 0

for i in range(0, len(t)-1):
    for j in range(len(t)):
        if j + i <= len(t):
            char = t[j:len(t) - i]
            print(char)
        if char in s:
            res = len(char)




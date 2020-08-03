k = input()
ik = int(k)

#sevens = [7, 77, 777, 7777, 77777, 777777, 7777777, 77777777, 777777777, 7777777777, 77777777777]


if k[0] not in ["1", "3" ,"7", "9"]:
    print(-1)
    exit()

for i in range(len(k), len(k) + 1000000):
    sev = "7" * i
    ise = int(sev)
    if ise % int(k) == 0:
        print(len(sev))
        exit()

print(-1)
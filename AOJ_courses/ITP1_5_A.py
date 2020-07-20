whs = []

while True:
    hw = list(map(int, input().split()))
    if hw[0] == 0 and hw[1] ==0:
        break
    whs.append(hw)

for i in range(len(whs)):
    h = whs[i][0]
    sqs = "#" * whs[i][1]
    for j in range(h + 1):
        if j == h:
            print("")
        else:
            print(sqs)

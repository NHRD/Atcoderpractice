whs = []

while True:
    hw = list(map(int, input().split()))
    if hw[0] == 0 and hw[1] ==0:
        break
    whs.append(hw)
#print(whs)

for i in range(len(whs)):
    w = whs[i][1]
    h = whs[i][0]
    moji = ""
    #print("h = {}" .format(h))
    #print("w = {}" .format(w))
    for j in range(h + 1):
        if j == h:
            moji = ""
        else:
            for k in range(w):
                if j % 2 == 0 and k % 2 == 0:
                    #print("in 1")
                    moji = moji + "#"
                elif j % 2 == 0 and k % 2 != 0:
                    #print("in 2")
                    moji = moji + "."
                elif j % 2 != 0 and k % 2 == 0:
                    #print("in 3")
                    moji = moji + "."
                elif j % 2 != 0 and k % 2 != 0:
                    #print("in 4")
                    moji = moji + "#"
             
        print(moji)
        moji = ""
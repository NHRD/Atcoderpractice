m = int(input())
mkm = m / 1000

if mkm > 70:
    print("89")
    exit()
if mkm >= 35 and mkm <= 70:
    print(str(((mkm - 30)/ 5) + 80)[:2])
    exit()
if mkm >= 6 and mkm <= 30:
    print(str(mkm + 50)[:2])
    exit()
if mkm >= 0.1 and mkm <= 5:
    mkm = mkm * 10
    if mkm < 10:
        print("0{}" .format(str(mkm)[:1]))
        exit()
    else:
        print(str(mkm)[:2])
        exit()

print("00")
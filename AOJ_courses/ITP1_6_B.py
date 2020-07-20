n = int(input())
i = 0
card = []
cards = []
while i < n:
    card = list(map(str, input().split()))
    cards.append(card)
    i += 1

#print(cards)

s = [i for i in range(1, 14)]
h = [i for i in range(1, 14)]
c = [i for i in range(1, 14)]
d = [i for i in range(1, 14)]

for i in range(n):
    card = cards[i]
    m = card[0]
    num = int(card[1])
    if m == "S":
        s.remove(num)
    elif m == "H":
        h.remove(num)
    elif m == "C":
        c.remove(num)
    else:
        d.remove(num)

for i in range(len(s)):
    (print("S {}" .format(s[i])))
for i in range(len(h)):
    (print("H {}" .format(h[i])))
for i in range(len(c)):
    (print("C {}" .format(c[i])))
for i in range(len(d)):
    (print("D {}" .format(d[i])))
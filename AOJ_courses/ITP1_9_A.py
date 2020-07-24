word = input()

sents = ""

while True:
    sent = input()
    if sent == "END_OF_TEXT":
        break
    sents = sents + " " + sent

words = list(map(str, sents.split()))
counts = 0

for w in words:
    w = w.lower()
    if w[len(w) - 1] == ".":
        w = w[:-1]
    if w == word:
        counts += 1

print(counts)
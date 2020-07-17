w = input()

res = ""

for i in range(len(w)):
    if w[i] not in ["a", "i", "u", "e", "o"]:
        res = res + w[i]

print(res)

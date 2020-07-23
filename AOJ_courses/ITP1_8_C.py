import string
import sys
#sent = ""
sent = sys.stdin.read()
"""while True:
    wd = input()
    if wd:
        sent = sent + wd
    else:
        break"""

sent = sent.lower()
#print(sent)
results = {let: sent.count(let) for let in set(sent)}
alphas = [chr(ord('a') + i) for i in range(26)]

for a in alphas:
    if a not in results:
        print("{} : {}" .format(a, 0))
    else:
        print("{} : {}" .format(a, results[a]))



results = []
grades = []

while True:
    result = list(map(int, input().split()))
    if result == [-1, -1, -1]:
        break
    results.append(result)
    
#print(results)

for i in range(len(results)):
    mid = results[i][0]
    ret = results[i][2]
    fin = results[i][1]
    if mid == -1 or fin == -1:
        grades.append("F")
    elif mid + fin >= 80:
        grades.append("A")
    elif mid + fin >= 65 and mid + fin < 80:
        grades.append("B")
    elif mid + fin >= 50 and mid + fin < 65:
        grades.append("C")
    elif mid + fin >= 30 and mid + fin < 50:
        if ret >= 50:
            grades.append("C")
        else:   
            grades.append("D")
    else:
        grades.append("F")
    
for i in range(len(results)):
    print(grades[i])
         
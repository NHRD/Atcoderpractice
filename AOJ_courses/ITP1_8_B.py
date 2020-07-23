results = []

while True:
    num = input()
    if int(num) == 0:
        for i in results:
            print(i)
        break
    nums = [int(i) for i in num]
    results.append(sum(nums))
    

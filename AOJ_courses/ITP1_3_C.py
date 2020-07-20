nsets = []
nset = []

while True:
    nset = list(map(int, input().split()))
    if nset[0] == 0 and nset[1] == 0:
        break
    nsets.append(nset)
    nset = []

for i in range(len(nsets)):
    nums = nsets[i]
    if nums[0] > nums[1]:
        print("{} {}" .format(nums[1], nums[0]))
    else:
        print("{} {}" .format(nums[0], nums[1]))
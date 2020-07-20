n = int(input())
nums = list(map(int, input().split()))
nums = sorted(nums)
sumnum = sum(nums)

print("{} {} {}" .format(nums[0], nums[len(nums)-1], sumnum))
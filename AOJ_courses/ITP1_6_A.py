n = int(input())
nums = list(map(int, input().split()))

for i in range(n):
    if i == n - 1:
        print("{}" .format(nums[n - i - 1])) 
    else:
        print("{}" .format(nums[n - i - 1]) ,end=" ")
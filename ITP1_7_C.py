r, c = map(int, input().split())

def num_get(r):
    nums = []
    for i in range(r):
        num = list(map(int, input().split()))
        nums.append(num)
    return nums

def hori_sum(nums, r):
    for i in range(len(r)):
        nums[i].append(sum(nums[i]))
        print(nums[i])
    returm nums

def verti_sum(nums, r, c):

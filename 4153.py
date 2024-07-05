import sys

while True:
    nums = list(map(int, sys.stdin.readline().split()))
    nums.sort()
    if sum(nums) == 0:
        break
    if nums[0]**2 + nums[1]**2 == nums[2]**2:
        print("right")
    else:
        print("wrong")

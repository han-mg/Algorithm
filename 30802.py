import sys
N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
T, P = map(int, sys.stdin.readline().split())
result = 0
for i in range(len(nums)):
    if nums[i] % T == 0:
        result += nums[i] // T
    else:
        result += nums[i] // T + 1
print(result)
print(N // P, N % P)
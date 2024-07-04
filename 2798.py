import sys

n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
r = 0
for i in range(n):
    for k in range(i+1, n):
        for j in range(k+1, n):
            if nums[i] + nums[k] + nums[j] > m:
                continue
            else:
                r = max(r, nums[i] + nums[k] + nums[j])
print(r)
import sys
N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
answer = 0
for i in range(N):
    cnt = 0
    if nums[i] == 1:
        continue
    for j in range(2, nums[i]+1):
        if nums[i] % j == 0:
            cnt += 1
    if cnt == 1:
        answer += 1
print(answer)
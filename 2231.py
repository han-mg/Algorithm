import sys
N = int(sys.stdin.readline())
for i in range(1, N+1):
    nums = i
    for k in str(i):
        nums += int(k)
    if nums == N:
        print(i)
        break
else:
    print(0)
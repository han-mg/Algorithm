import sys, heapq
n = int(sys.stdin.readline())
h = []
for i in range(n):
    nums = list(map(int, sys.stdin.readline().split()))
    for j in nums:
        heapq.heappush(h, j)
        if len(h) > n:
            heapq.heappop(h)
print(h[0])
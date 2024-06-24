import sys
n, w, L = map(int, sys.stdin.readline().split())
truck = list(map(int, sys.stdin.readline().split()))

q = [0] * w
time = 0
while q:
    time += 1
    q.pop(0)
    if truck:
        if sum(q) + truck[0] <= L:
            q.append(truck.pop(0))
        else:
            q.append(0)
print(time)
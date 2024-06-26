import sys

n, k, m = map(int, sys.stdin.readline().split())
l = []
for i in range(n):
    g = int(sys.stdin.readline())
    if g > 2 * k:
        l.append(g-(2*k))
    elif g < 2 * k and g - k > 0:
        l.append(g-k)
if len(l) == 0:
    print(-1)
    exit()

p = -1
s = 1
e = max(l)
while s <= e:
    mid = (s + e) // 2
    t = 0
    for i in l:
        t += i // mid
    if t < m:
        e = mid - 1
    else:
        s = mid + 1
        p = mid

print(p)
import sys
sys.setrecursionlimit(10**9)
N = int(sys.stdin.readline())

def dfs(v):
    visited[v] = 1
    for i in range(len(adj_list[v])):
        n = adj_list[v][i][0]
        if not visited[n]:
            d[n] = adj_list[v][i][1] + d[v]
            dfs(n)

visited = [0 for i in range(N+1)]
adj_list = [[] for i in range(N+1)]
d = [0 for i in range(N+1)]
for i in range(1, N):
    a, b, c = map(int, sys.stdin.readline().split())
    adj_list[a].append([b, c])
    adj_list[b].append([a, c])

dfs(1)
print(max(d))
#-------------------------------------------------------------
import sys
from collections import deque

N = int(sys.stdin.readline().strip())

def bfs(start):
    visited[start] = 1
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for w, dist in adj_list[v]:
            if not visited[w]:
                visited[w] = 1
                d[w] = d[v] + dist
                queue.append(w)

visited = [0 for _ in range(N + 1)]
adj_list = [[] for _ in range(N + 1)]
d = [0 for _ in range(N + 1)]

for _ in range(N - 1):
    a, b, c = map(int, sys.stdin.readline().strip().split())
    adj_list[a].append((b, c))
    adj_list[b].append((a, c))

bfs(1)
print(max(d))

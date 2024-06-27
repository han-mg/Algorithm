import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())
g = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    g[a].append(b)
    g[b].append(a)
    g[a].sort()
    g[b].sort()

def dfs(g, v, visited):
    visited[v] = True
    print(v, end=' ')
    for j in g[v]:
        if not visited[j]:
            dfs(g, j, visited)

def bfs(g, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for k in g[v]:
            if not visited[k]:
                queue.append(k)
                visited[k] = True

visited = [False] * (N+1)
dfs(g, V, visited)
print("")
visited = [False] * (N+1)
bfs(g, V, visited)
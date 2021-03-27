def bipartite(adj):
    n = len(adj)
    color = [0]*n
    for i in range(len(adj)):
        if color[i]: continue
        color[i] =1
        
    return True


import sys
input = sys.stdin.readline
K = int(input())
for i in range(K):
    V, E = map(int,input().split())
    path = [[] for k in range(V)]
    for j in range(E):
        a, b = map(int,input().split())
        path[a-1].append(b-1)
        path[b-1].append(a-1)
    path.sort()
    bipartite(path)


n = 0 #노드갯수
from collections import deque
def bipartite(adj):
    color = [0]*(n+1); Q = deque()
    for v in range(n+1):
        if color[v]: continue
        color[v] = 1; Q.append(v)
        while Q:
            p = Q.popleft()
            for q in adj[p]:
                if color[q] and color[p] == color[q]: return False
                if color[q]: continue
                color[q] = 3-color[p]; Q.append(q)
    return True  
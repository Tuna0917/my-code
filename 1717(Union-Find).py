import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m = map(int,input().split())
parent = list(range(n+1))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    parent[find(x)] = find(y)


for i in range(m):
    k,a,b = map(int,input().split())
    if k:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
    else:
        union(a,b)
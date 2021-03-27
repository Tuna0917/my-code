'''
N = 노드갯수
M = 간선갯수
V = 시작노드
'''

N, M, V= map(int,input().split())

visited = [False]*(N+1)
able = [[]]
lists = []
for i in range(M):
    lists.append(input())
lists.sort()
for i in range(N):
    able.append(list())

for nodes in lists:
    x, y = map(int, nodes.split())
    able[x].append(y)
    able[y].append(x)


stack =[V]
visited[V] = True
answer = []
while stack:
    start_node = stack.pop(0)
    for node in able[start_node]:
        if not visited[node]:
            visited[node] = True
            stack.append(node)
    answer.append(start_node)

print(answer)


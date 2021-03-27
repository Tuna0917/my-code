'''
N = 노드갯수
M = 간선갯수
V = 시작노드
'''

N, M, V= map(int,input().split())

visited = [False]*(N+1)
links = [[]]
lists = []
for i in range(M):
    lists.append(input())
lists.sort()
for i in range(N):
    links.append(list())

for nodes in lists:
    x, y = map(int, nodes.split())
    links[x].append(y)
    links[y].append(x)


stack =[V]
visited[V] = True
answer = []
while stack:
    start_node = stack.pop(0)
    visited[start_node] = True
    new_stack = []
    for node in links[start_node]:
        if not visited[node]:
            new_stack.append(node)
    for node in stack:
        if not node in new_stack and not visited[node]:
            new_stack += [node]
    stack = new_stack
    answer.append(start_node)

print(answer)

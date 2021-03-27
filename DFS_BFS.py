def DFS(links, V):
    answer = []

    visited = [False]*(N+1)
    stack =[V]
    visited[V] = True

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

    print(' '.join(map(str, answer)))

def BFS(links, V):
    answer = []

    visited = [False]*(N+1)
    stack =[V]
    visited[V] = True

    while stack:
        start_node = stack.pop(0)
        for node in links[start_node]:
            if not visited[node]:
                visited[node] = True
                stack.append(node)
        answer.append(start_node)

    print(' '.join(map(str, answer)))

N, M, V= map(int,input().split())

links = [[]]
lists = []
for i in range(M):
    lists.append(input())
lists.sort()
for i in range(N):
    links.append(list())

for nodes in lists:
    x, y = map(int, nodes.split())
    if not y in links[x]:
        links[x].append(y)
    if not x in links[y]:
        links[y].append(x)

link1 = links.copy()
link2 = links.copy()
DFS(link1, V)

BFS(link2, V)
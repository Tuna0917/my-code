N = int(input())
M = int(input())
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


stack =[1]
visited[1] = True
answer = []
while stack:
    start_node = stack.pop(0)
    for node in able[start_node]:
        if not visited[node]:
            visited[node] = True
            stack.append(node)
    answer.append(start_node)

print(len(answer)-1) #1번은 제외해야해서
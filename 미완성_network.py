def solution(n, computers):
    answer = 0
    visited = [False]*n
    i=0
    x = True
    while x:
        old = visited.copy()
        link(i,computers,visited)
        if old != visited:
            answer += 1
        i += 1
        if not False in visited:
            x = False
    
    return answer

def link(k, computers, visited):
    if visited[k] == False:
        visited[k] = True
    for i, connect in enumerate(computers[k]):
        if connect:
            if visited[i] == False:
                link(i, computers, visited)
'''
이야 처음부터 잘 짯었네;;
'''
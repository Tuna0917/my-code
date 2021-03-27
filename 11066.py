import heapq
T = int(input())
for i in range(T):
    K = int(input())
    files = list(map(int, input().split()))
    heapq.heapify(files)
    pop = heapq.heappop
    push = heapq.heappush
    answer = 0
    while 1:
        f1,f2 = pop(files), pop(files)
        new_f = f1+f2
        answer += f1+f2
        if not files:
            break
        push(files, new_f)
    print(answer)
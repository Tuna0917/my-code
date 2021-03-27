'''
0 = 0
1 = 0
2 = 1
3 = 1
4 = 2

N = N//2
'''
import heapq
import sys

input=sys.stdin.readline

N = int(input())
max_heap = []
min_heap = []

push = heapq.heappush
pop = heapq.heappop
for i in range(N):
    num = int(input())
    '''
    여기서 answer을 정렬할 무언가가 필요함
    그것도 매우 단순하고 빠르게
    우선순위큐 그거...
    제일 작은값이나 제일큰값 구할때나 쓸모있지않나?
    얘처럼 중간값 구할떄는 어떻게 사용하지?
    Max heap이랑 Min heap을 써볼까
    Maxheap의 꼭대기 <= Minheap의 꼭대기로
    '''
    if i == 0: #i=0,2,4,8
        push(max_heap, -num)
    elif i%2 == 0:
        if num < min_heap[0]:
            push(max_heap, -num)
        else:
            push(max_heap, -pop(min_heap))
            push(min_heap, num)
    else:
        if -max_heap[0] < num:
            push(min_heap, num)
        else:
            push(min_heap, -pop(max_heap))
            push(max_heap, -num)

    print(-max_heap[0])

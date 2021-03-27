N, M = map(int,input().split())

from itertools import combinations

answer = combinations([i+1 for i in range(N)], M)
for tup in answer:
    print(' '.join(map(str,tup)))
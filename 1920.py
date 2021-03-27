A = dict()
N = int(input())
for a in map(int,input().split()):
    A[a] = True
M = int(input())
for a in map(int,input().split()):
    if A.get(a, False):
        print(1)
    else:
        print(0)


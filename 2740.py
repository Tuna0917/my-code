def multiple(l1:list,l2:list):
    answer = 0
    for i in range(len(l1)):
        answer += l1[i]*l2[i]
    return answer

N, M = map(int,input().split())
A = []

for i in range(N):
    A.append(list(map(int,input().split())))
M, K = map(int,input().split())
B =[]
for i in range(K):
    B.append([0]*M)


for i in range(M):
    for j, x in enumerate(list(map(int,input().split()))):
        B[j][i] = x

answer = []
for i in range(N):
    answer.append([0]*K)
for i in range(N):
    for j in range(K):
        answer[i][j] = str(multiple(A[i],B[j]))

for li in answer:
    print(' '.join(li))


answer=[[0],[1],[2,4,8,6],[3,9,7,1],[4,6],[5],[6],[7,9,3,1],[8,4,2,6],[9,1]]

T = int(input())
for i in range(T):
    a, b = map(int,input().split())
    ans = answer[a%10][b%len(answer[a%10])-1]
    if ans == 0:
        print(10)
    else:
        print(ans)
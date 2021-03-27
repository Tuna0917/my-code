'''
입력
첫째 줄에는 전체 종이의 한 변의 길이 N이 주어져 있다. N은 2, 4, 8, 16, 32, 64, 128 중 하나이다. 색종이의 각 가로줄의 정사각형칸들의 색이 윗줄부터 차례로 둘째 줄부터 마지막 줄까지 주어진다. 
하얀색으로 칠해진 칸은 0, 파란색으로 칠해진 칸은 1로 주어지며, 각 숫자 사이에는 빈칸이 하나씩 있다.

출력
첫째 줄에는 잘라진 햐얀색 색종이의 개수를 출력하고, 둘째 줄에는 파란색 색종이의 개수를 출력한다.

'''
def cut(double_list:list):
    N = len(double_list)

    if N ==1:
        if double_list[0][0] == 1:
            return [0,1]
        else:
            return [1,0]

    n = N//2
    total = 0
    for line in double_list:
        total += sum(line)
    if total == N*N: #파랑
        return [0,1]  
    elif total == 0: #하양
        return [1,0]
    else: #4등분
        I = [quater[:n] for quater in double_list[:n]]
        II = [quater[n:] for quater in double_list[:n]]
        III = [quater[:n] for quater in double_list[n:]]
        IV = [quater[n:] for quater in double_list[n:]]
        return [cut(I)[0] + cut(II)[0] + cut(III)[0] + cut(IV)[0], cut(I)[1] + cut(II)[1] + cut(III)[1] + cut(IV)[1]]
 
N = int(input())
sheet = []
for i in range(N):
    sheet.append(list(map(int,input().split())))

answer = cut(sheet)
for x in answer:
    print(x)
WANT1 = [
    ['B','W','B',"W",'B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B',"W",'B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B',"W",'B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B',"W",'B','W','B','W'],
    ['W','B','W','B','W','B','W','B']
]
WANT2 = [
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B',"W",'B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B',"W",'B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B',"W",'B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B',"W",'B','W','B','W']
]

N,M= map(int,input().split())
table = []
for i in range(N):
    table.append(list(input()))
answer = -1
for y in range(N-7):
    for x in range(M-7):
        change_1 = 0
        change_2 = 0
        for j in range(8):
            for i in range(8):
                if WANT1[j][i] != table[y+j][x+i]:
                    change_1 += 1
                if WANT2[j][i] != table[y+j][x+i]:
                    change_2 += 1
            changed = min(change_1,change_2)
        if answer == -1:
            answer = changed
        else:
            answer = min(answer, changed)
print(answer)
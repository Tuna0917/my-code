def solution(n, results):
    answer = [0]*n
    ranking = dict()
    for i in range(n):
        ranking[i+1] = []
    for fight in results:
        winner = fight[0]
        loser = fight[1]
        ranking[loser].append(winner)
        for people in ranking[winner]:
            if not people in ranking[loser] and people>0:
                ranking[loser].append(people)
        ranking[winner].append(-loser)
        for people in ranking[loser]:
            if not people in ranking[winner] and people<0:
                ranking[winner].append(people)
    
    for rank in ranking:
        answer[rank-1]=ranking[rank]
    k=0
    for x in answer:
        if len(x) == n-1:
            k += 1
    return k

solution(5,[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])
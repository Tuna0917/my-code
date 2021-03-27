def tjfxkdqoekf(N):
    for i in range(N//5,-1,-1):
        if(N-i*5)%3==0:
            return (N-i*5)//3 +i
    return -1

print(tjfxkdqoekf(int(input())))
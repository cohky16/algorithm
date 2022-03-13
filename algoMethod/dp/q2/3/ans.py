n=int(input())
A=[list(map(int,input().split())) for _ in range(n)]
ans = [[0]*3 for _ in range(n)]
ans[0] = A[0]
for i in range(1, n):
    for j in range(3):
        if j == 0: ans[i][j] += max(ans[i-1][j+1],ans[i-1][j+2]) + A[i][0]
        if j == 1: ans[i][j] += max(ans[i-1][j-1],ans[i-1][j+1]) + A[i][1]
        if j == 2: ans[i][j] += max(ans[i-1][j-2],ans[i-1][j-1]) + A[i][2]
print(max(ans[-1]))



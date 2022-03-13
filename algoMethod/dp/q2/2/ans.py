n=int(input())
A=list(map(int, input().split()))
ans=[[0]*n for _ in range(n)]
ans[0]=A
for i in range(1,n):
    for j in range(n):
        ans[i][j] += ans[i-1][j]
        if j > 0: ans[i][j] += ans[i-1][j-1]
        if j < n-1: ans[i][j] += ans[i-1][j+1]
        ans[i][j] %= 100
print(ans[-1][-1])


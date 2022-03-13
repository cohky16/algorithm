n=int(input())
A=[list(map(int,input().split())) for _ in range(n)]
ans=[[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        ans[i][j] += (max(ans[i-1][j], ans[i][j-1])+A[i][j])
print(ans[-1][-1])

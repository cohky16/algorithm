n,m=map(int,input().split())
wlist=list(map(int,input().split()))
vlist=list(map(int,input().split()))
dp=[[-1]*(m+1) for _ in range(n+1)]
dp[0][0] = 0
for i in range(n):
    for j in range(m+1):
        if dp[i][j] < 0: continue
        # 下に配る
        dp[i+1][j]=max(dp[i+1][j], dp[i][j])
        if j+wlist[i] <= m:
            dp[i+1][j+wlist[i]]=max(dp[i+1][j+wlist[i]], dp[i][j]+vlist[i])
# 最下層の最大値
print(max(dp[-1]))

n,m=map(int,input().split())
wlist=list(map(int,input().split()))
dp=[[1010101]*(m+1) for _ in range(n+1)]
dp[0][0]=0
# 0 INF INF INF INF INF
# 0 INF 1 INF INF INF
# 0 INF 1 INF INF 1
# 0 INF 1 1 INF 2
for i in range(n):
    for j in range(m+1):
        if dp[i][j] == 1010101: continue
        # 下に最小値
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])
        # 右下に最小値
        if j+wlist[i] <= m:
            dp[i+1][j+wlist[i]] = min(dp[i+1][j+wlist[i]], dp[i][j]+1)
# 重さMで判定
print(dp[-1][-1] if dp[-1][-1] != 1010101 else -1)

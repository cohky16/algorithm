n,m=map(int,input().split())
alist=list(map(int,input().split()))
blist=list(map(int,input().split()))
dp=[[-1]*m for _ in range(n)]
dp[0][0] = 0
for i in range(n-1):
    for j in range(m):
        # 到達不可能コマ
        if dp[i][j] < 0: continue
        # 暫定スコアより高く渡せるなら渡す
        dp[i+1][j] = max(dp[i+1][j],dp[i][j])
        if j+alist[i] < m:
            dp[i+1][j+alist[i]] = max(dp[i+1][j+alist[i]], dp[i][j]+blist[i])
print(dp[-1][-1])

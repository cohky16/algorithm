n,m=map(int,input().split())
wlist=list(map(int,input().split()))
dp=[[False]*(m+1) for _ in range(n+1)]
dp[0][0] = True
# 1,0,0,0,0 -> 0: 0
# 1,1,0,0,0 -> 1: 0+1
# 1,1,1,1,0 -> 2: 1,0+2,1+2
# 1,1,1,1,1 -> 3: 1,2,0+3,1+3
for i in range(n):
    for j in range(m+1):
        if not dp[i][j]: continue
        # 下
        dp[i+1][j] = True
        # 右下
        if j+wlist[i] <= m:
            dp[i+1][j+wlist[i]] = True
print("Yes" if dp[n][m] else "No")

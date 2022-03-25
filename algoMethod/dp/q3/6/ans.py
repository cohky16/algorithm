n,a,b=map(int,input().split())
xlist=list(map(int,input().split()))
if b == 0: print("Yes")
else:
    dp=[[False]*a for _ in range(n+1)]
    dp[0][0]=True
    # 1 0 0 0 0 0 0 0 0 0
    # 1 1 0 0 0 0 0 0 0 0
    # 1 1 0 1 1 0 0 0 0 0
    # 1 1 0 1 1 0 1 1 0 1
    # 1 1 1 1 1 1 1 1 1 1
    for i in range(n):
        for j in range(a):
            if not dp[i][j]: continue
            dp[i+1][j] = dp[i][j]
            dp[i+1][(j+xlist[i])%a] = True
    print("Yes" if dp[-1][b] else "No")

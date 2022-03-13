n=int(input())
A=[list(map(int,input().split())) for _ in range(n)]
INF=1010101
ans=[[INF]*n for _ in range(n)]
ans[0][n-1] = A[0][n-1]
for i in range(n):
    for j in reversed(range(n)):
            # 上からと右からでどっちが小さいか処理するために本体と比較する
            if i >= 1: ans[i][j] = min(ans[i][j], ans[i-1][j] + A[i][j])
            if j < n-1: ans[i][j] = min(ans[i][j], ans[i][j+1] + A[i][j])
print(ans[-1][0])


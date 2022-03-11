n,m=map(int,input().split())
dlist=list(map(int,input().split()))
# 0~nまでのマス
dp=[0]*(n+1)
# 0にははじめからいる
dp[0]=1
# マスの数
for i in range(1, n + 1):
    # サイコロの数
    for j in range(m):
        # サイコロが超えないかと、残りのマスが既に埋められているか
        # 最初はぴったしのを埋めて、残りはand以下で判定を繰り返す
        if i - dlist[j] >= 0 and dp[i - dlist[j]]:
            dp[i] = 1
print("Yes" if dp[n] else "No")


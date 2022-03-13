n=int(input())
ans=[[0]*n for _ in range(n)]
# 初期化
ans[0][0]=1
# マスごとにたどりつく道筋の数を求める
for i in range(n):
    for j in range(n):
        # 上からの場合
        if i >= 1 and ans[i-1][j] >= 1: ans[i][j] += ans[i-1][j]
        # 左からの場合
        if j >= 1 and ans[i][j-1] >= 1: ans[i][j] += ans[i][j-1]
print(ans[-1][-1])

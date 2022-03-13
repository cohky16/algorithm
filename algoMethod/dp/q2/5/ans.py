n=int(input())
S=[list(input()) for _ in range(n)]
if S[0][0] == "#": print(0)
else:
    ans=[[0]*n for _ in range(n)]
    ans[0][0] = 1
    for i in range(n):
        for j in range(n):
            # 穴の場合
            if S[i][j] == "#":
                continue
            # 上
            if i >= 1 and S[i-1][j] != "#": ans[i][j] += ans[i-1][j]
            # 左
            if j >= 1 and S[i][j-1] != "#": ans[i][j] += ans[i][j-1]
    print(ans[-1][-1])



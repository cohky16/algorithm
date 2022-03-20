n,m=map(int,input().split())
alist=list(map(int,input().split()))
ans=[[0]*m for _ in range(n)]
ans[0][0] = 1
for i in range(1, n):
    for j in range(m):
        ans[i][j] += ans[i-1][j]
        t = j + alist[i-1]
        if t < m: ans[i][t] += ans[i-1][j]
print(sum([1 for a in ans[-1] if a > 0]))

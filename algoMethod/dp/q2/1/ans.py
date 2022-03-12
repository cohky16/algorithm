A=list(map(int,input().split()))
ans=[[0]*4 for _ in range(4)]
ans[0] = A
for i in range(1,4):
    for j in range(4):
        ans[i][j] += ans[i-1][j]
        if j > 0:
            ans[i][j] += ans[i-1][j-1]
        if j < 3:
            ans[i][j] += ans[i-1][j+1]
print(ans[3][3])

n=int(input())
wlist=list(map(int,input().split()))
total=sum(wlist)
dpa=[[-1]*(total+1) for _ in range(n+1)]
dpb=[[total]*(total+1) for _ in range(n+1)]
# 0 -1 -1 -1 -1 -1
# 1 -1 -1 -1 -1 -1
# 1 -1 3 4 -1 -1
# 1 2 3 4 5 6

# 6 6 6 6 6 6
# 5 6 6 6 6 6
# 5 6 3 2 6 6
# 5 4 3 2 1 0
dpa[0][0]=0
for i in range(n):
    for j in range(total):
        if dpa[i][j] < 0: continue
        dpa[i+1][j]=max(dpa[i+1][j],dpa[i][j])
        dpb[i+1][j]=total-dpa[i+1][j]
        if j+wlist[i] <= total:
            dpa[i+1][j+wlist[i]]=max(dpa[i+1][j+wlist[i]],dpa[i][j]+wlist[i])
            dpb[i+1][j+wlist[i]]=total-dpa[i+1][j+wlist[i]]
ans=1010101
for a,b in zip(dpa[-1],dpb[-1]):
    ans = min(ans, abs(a-b))
print(ans)

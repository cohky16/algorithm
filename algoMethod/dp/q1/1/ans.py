n,x,y=map(int, input().split())
ans = [x,y]
for i in range(2,n):
    ans.append((ans[i-2]+ans[i-1])%100)
print(ans[n-1])

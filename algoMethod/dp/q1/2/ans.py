n=int(input())
alist=list(map(int, input().split()))
ans=[0]*n
ans[1]=alist[1]
for i in range(2,n):
    ans[i] = min(ans[i-1]+alist[i], ans[i-2]+alist[i]*2)
print(ans[-1])


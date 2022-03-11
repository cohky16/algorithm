n,m=map(int,input().split())
alist=list(map(int,input().split()))
ans=[1000000]*n
# 最初のマスは0
ans[0]=0
# 進むたびに後ろを計算　
for i in range(1,n):
    # m個前まで計算
    for j in range(1,m+1):
        # 数を超えないように
        if i-j >= 0:
            # そのマスの最小値を求めるため、iで固定してjで前のマスを指定する
            ans[i] = min(ans[i],ans[i-j]+alist[i]*j)
print(ans[-1])

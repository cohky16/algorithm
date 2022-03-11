n=int(input())
l=[1,1,2]
for i in range(3,n+1):
    l.append(l[i-3]+l[i-2]+l[i-1])
print(l[n])


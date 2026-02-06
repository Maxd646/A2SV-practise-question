n, k =map(int, input().split())
arra=list(map(int, input().split()))
count=0
m=arra[k-1]
for i in range(len(arra)):
    if arra[i]>=m and arra[i]>0: 
        count+=1
print(count)
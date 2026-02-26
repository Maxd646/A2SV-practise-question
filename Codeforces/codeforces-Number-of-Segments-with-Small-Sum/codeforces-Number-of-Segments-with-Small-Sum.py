# Number of Segments with Small Sum
# Platform: Codeforces
n, m = map(int, input().split())
aa= list(map(int, input().split()))
ans=0
summ=0
left=0
for right in range(len(aa)):
    summ+=aa[right]
    while summ>m:
        summ-=aa[left]
        left+=1
    ans+=right-left+1
print(ans)

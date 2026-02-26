# (D) Number of Segments with Big Sum
# Platform: Codeforces
n, m= map(int, input().split())
aa= list(map(int, input().split()))
summ=0
ans=0
mm=len(aa)
left=0
for i in range(len(aa)):
    summ+=aa[i]
    while summ>=m:
        ans+=(mm-i)
        summ-=aa[left]
        left+=1
print(ans)

# E. Segments with Small Set
# Platform: Codeforces
from collections import defaultdict
n, k= map(int, input().split())
aa= list(map(int, input().split()))
count= defaultdict(int)
ans=0
left=0
dic=0
for r in range(len(aa)):
    if count[aa[r]]==0:
        dic+=1
    count[aa[r]]+=1
    while dic>k:
        count[aa[left]]-=1
        if count[aa[left]]==0:
            dic-=1
        left+=1
    ans+=r-left+1
print(ans)
        

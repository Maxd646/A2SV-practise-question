# (C) Number of Equal
# Platform: Codeforces
n, m= map(int, input().split())
aa= list(map(int, input().split()))
bb= list(map(int, input().split()))
from collections import Counter
mm= Counter(bb)
ans=0
for i in range(len(aa)):
    ans+=mm[aa[i]]
print(ans)

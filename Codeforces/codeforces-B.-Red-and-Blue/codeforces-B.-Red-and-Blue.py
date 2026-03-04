# B. Red and Blue
# Platform: Codeforces
from itertools import accumulate
for _ in range(int(input())):
    input()
    aa=list(map(int, input().split()))
    input()
    bb=list(map(int, input().split()))
    ans=max(max(list(accumulate(aa))), 0)+ max(max(list(accumulate(bb))), 0)
    
    print(ans if ans>=0 else 0 )
    

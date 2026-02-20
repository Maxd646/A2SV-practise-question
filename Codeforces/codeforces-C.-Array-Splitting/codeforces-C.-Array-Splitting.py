# C. Array Splitting
# Platform: Codeforces
n, m= map(int, input().split())
aa= list(map(int, input().split()))
if m==1:
    print(max(aa)- min(aa))
elif len(aa)==m:
    print(0)
else:
    c= [aa[i]-aa[i-1] for i in range(1, len(aa))]
    c.sort()
    res=0
    for i in range(len(c)-m+1):
        res+=c[i]
    print(res)


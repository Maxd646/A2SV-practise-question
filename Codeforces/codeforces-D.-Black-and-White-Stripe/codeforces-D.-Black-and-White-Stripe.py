# D. Black and White Stripe
# Platform: Codeforces
for _ in range(int(input())):
    n, k= map(int, input().split())
    s= input()
    if "B"*k in s:
        print(0)
    elif len(s)==k:
        print(s.count("W"))
    elif s.count("B")==0:
        print(k)
    else:
        left=0
        ans= k
        summ=0
        for r in range(n):
            if s[r]=="B":
                summ+=1
            if r-left+1>=k:
                ans= min(ans, k-summ)
                summ-=(1 if s[left]=="B" else 0)
                left+=1
        print(ans)
            


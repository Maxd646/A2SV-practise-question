for _ in range(int(input())):
    s= input()
    n = len(s)
    ans=[]
    nu =0
    for i in range(n):
        if s[i]!="0":
            ans.append(int(s[i]+"0"*(n-i-1)))
            nu+=1
    print(nu)
    print(*ans)
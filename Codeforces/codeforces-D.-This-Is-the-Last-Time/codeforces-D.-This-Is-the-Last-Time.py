# D. This Is the Last Time
# Platform: Codeforces
 for _ in range(int(input())):
    n, k=map(int, input().split())
    arra=[]
    for _ in range(n):
        aa=list(map(int, input().split()))
        arra.append(aa)
    arra.sort()
    for i in range(n):
        if arra[i][0]<=k<=arra[i][1]:
            k=max(arra[i][2], k)
    print(k)

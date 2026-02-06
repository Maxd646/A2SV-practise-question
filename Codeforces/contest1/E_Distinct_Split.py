n= int(input())
for _ in range(n):
    t=int(input())
    aa=input().strip()
    pre=[0]*t
    seen=set()
    for i in range(len(aa)):
        seen.add(aa[i])
        pre[i]=len(seen)
    seen2=set()
    
    back=[0]*t
    for i in range(len(aa)-1, -1, -1):
        seen2.add(aa[i])
        back[i]=len(seen2)
    maxx=0
    for i in range(t-1):
        maxx=max(maxx, back[i+1]+pre[i])
    print(maxx)
    


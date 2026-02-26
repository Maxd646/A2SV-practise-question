# B. Most socially-distanced subsequence
# Platform: Codeforces

for _ in range(int(input())):
    n= int(input())
    aa= list(map(int, input().split()))   
    ans=[]
    ans.append(aa[0])
    for i in range(1, len(aa)-1):
        if aa[i-1]<aa[i] and aa[i]>aa[i+1] or aa[i-1]>aa[i] and aa[i]<aa[i+1] :
            ans.append(aa[i])
    if ans[-1]!=aa[-1]:
        ans.append(aa[-1])
    print(len(ans))
    print(*ans)

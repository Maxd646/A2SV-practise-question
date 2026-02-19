# B. Optimal Point on a Line
# Platform: Codeforces
input()
aa= list(map(int, input().split()))
aa.sort()
if len(aa)%2==0:
    print(aa[len(aa)//2-1])
else:
    print(aa[len(aa)//2])

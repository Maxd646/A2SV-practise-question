n = int(input())
aa= [[] for _ in range(n + 1)]
for i in range(2, n + 1):
    root = int(input())
    aa[root].append(i)
found= False
for i in range(1, n + 1):
    if aa[i]:  
        count = 0
        for c in aa[i]:
            if len(aa[c])==0:
                count+= 1
        if count < 3:
            found=True
            print("No")
            break
    else:
        continue
if not found:
    print("Yes")
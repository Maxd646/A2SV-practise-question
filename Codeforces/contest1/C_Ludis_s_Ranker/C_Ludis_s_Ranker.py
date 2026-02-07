from collections import Counter
n= int(input())
s= list(map(int, input().split()))
count=Counter(s)
res = sorted(count.items(), key=lambda x:x[0], reverse=True)
seen=Counter()
rank=1
for ch, num in res:
    seen[ch]=rank
    rank+=num
result=[]
for i in range(len(s)):
    result.append(str(seen[s[i]]))
re= " ".join(result)
print(re)






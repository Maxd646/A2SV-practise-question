# A Needle in a Haystack
# Platform: Codeforces
from collections import  Counter
for _ in range(int(input())):
    t=input()
    s=input()
    count=Counter(s)-Counter(t)
    if  not Counter(s)>=Counter(t):
        print("Impossible")
    else:
        res= sorted(count.items())
        letter=[]
        for ch, num in res:
            letter.append(ch*num)
        res="".join(letter)
        ans=[]
        i=0
        for ch in res:
            while i<len(t) and t[i]<=ch:
                ans.append(t[i])
                i+=1
            ans.append(ch)
        # remining 
        while i<len(t):
            ans.append(t[i])
            i+=1
    
        print("".join(ans))


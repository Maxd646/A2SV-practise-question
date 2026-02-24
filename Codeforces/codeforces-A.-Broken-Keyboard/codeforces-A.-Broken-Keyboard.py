# A. Broken Keyboard
# Platform: Codeforces
for _ in range(int(input())):
    a=input()
    ans=[]
    i=0
    if len(a)==1:
        ans.append(a[0])
    else:
        while i<len(a)-1:
            if a[i]==a[i+1]:
                i+=2
            else:
                ans.append(a[i])
                i+=1
    res="".join(ans)+(a[i:] if len(a)>1 else "")
    print("".join(sorted(list(set(res)))))


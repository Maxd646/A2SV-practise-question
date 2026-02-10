# C. Dominant Character
# Platform: Codeforces

for _ in range(int(input())):
    input()
    s= input()
    if "aa" in s:
         print(2)
    else:
        if  "aca" in s or "aba" in s:
            print(3)
        elif  "abca" in s or "acba" in s:
            print(4)
        elif "abbacca" in s or "accabba" in s:
            print(7)
        else:
            print(-1)
          

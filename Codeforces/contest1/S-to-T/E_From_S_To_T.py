from collections import Counter
 
def name(s, t):
    i = 0
    for ch in t:
        if i < len(s) and ch == s[i]:
            i += 1
    return i == len(s)
 
 
for _ in range(int(input())):
    s = input().strip()
    t = input().strip()
    p = input().strip()
 
   
    if not name(s, t):
        print("NO")
        continue
 
   
    need = Counter(t) - Counter(s)
    have = Counter(p)
 
    print("YES" if all(have[c] >= need[c] for c in need) else "NO")
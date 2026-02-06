# B. Rebranding
# Platform: Codeforces

n, m= map(int, input().split())
name=input().strip()
seen = {}
for a in name:
    seen[a]=a
for _ in range(m):
    s, t= input().split()
    for ch in seen:
        if seen[ch]==s:
            seen[ch]=t
        elif seen[ch]==t:
            seen[ch]=s
answer= "".join(seen[ch] for ch in name)
print(answer)


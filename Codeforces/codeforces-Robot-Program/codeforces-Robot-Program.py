# Robot Program
# Platform: Codeforces

for _ in range(int(input())):
    n, x, k = map(int, input().split())
    s = input().strip()
    
    pr = 0
    f = -1
    
    for i in range(n):
        if s[i] == 'L':
            pr -= 1
        else:
            pr += 1
        
        if pr== -x:
            f = i + 1
            break
    
    if f== -1 or f > k:
        print(0)
        continue
    
    an= 1
    r= k - f
    
    pr = 0
    cy= -1
    
    for i in range(n):
        if s[i] == 'L':
            pr-= 1
        else:
            pr += 1
        
        if pr == 0:
            cy = i + 1
            break
    
    if cy == -1:
        print(an)
    else:
        an += r // cy
        print(an)

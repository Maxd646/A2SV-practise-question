for i in range(int(input())):
    s= input().strip()
    found=False
    for i in range(len(s)-1):
        if s[i+1]!="0" and int(s[:i+1])<int(s[i+1:]):
            print(s[:i+1]+ " " +s[i+1:])
            found=True
            break
    if not found:
        print(-1)
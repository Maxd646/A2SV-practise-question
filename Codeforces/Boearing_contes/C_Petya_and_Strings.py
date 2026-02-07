n= input().strip()
t=input().strip()
found=False
for i in range(len(n)):
    if n[i].lower()>t[i].lower():
        print(1)
        found=True
        break
    elif n[i].lower()<t[i].lower():
        print(-1)
        found=True
        break
if not found:
    print(0)


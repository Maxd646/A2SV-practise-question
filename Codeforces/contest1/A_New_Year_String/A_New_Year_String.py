t= int(input())
for _ in range(t):
    n= int(input())
    arra= input().strip()
    seen=set()
    found=False
    for i in range(len(arra)-3):
        seen.add(arra[i:i+4])
        if "2026" in seen:
            print(0)
            found=True
            break
    if not found: 
        if "2025" in seen:
            print(1)
        else:
            print(0)



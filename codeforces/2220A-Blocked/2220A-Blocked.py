for _ in range(int(input())):
    n = int(input())
    arra = list(map(int, input().split()))
    
    arra = sorted(arra, reverse=True)
    p = set()
    found = True
    for num in arra:
        if num in p:
            print(-1)
            break
        p.add(num)
    else:
        print(*arra)
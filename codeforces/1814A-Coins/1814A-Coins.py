for _ in range(int(input())):
    n, k = map(int, input().split())
    if (n-k)%2==1 and k%2!=1:
        print("NO")
        continue
    print("YES")
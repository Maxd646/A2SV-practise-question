for _ in range(int(input())):
    n = int(input())
    aa = list(map(int, input().split()))
    a = sum(1 for i in range(n) if aa[i]%2==0)
    print(min(a, n-a))
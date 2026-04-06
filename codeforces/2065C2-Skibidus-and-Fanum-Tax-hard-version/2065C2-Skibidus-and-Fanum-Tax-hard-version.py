from bisect import bisect_left

for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = sorted(list(map(int, input().split())))

    prev = -10**30
    ok = True

    for i in range(n):
        possible = []

        if a[i] >= prev:
            possible.append(a[i])

        idx = bisect_left(b, prev + a[i])
        if idx < m:
            possible.append(b[idx] - a[i])

        if not possible:
            ok = False
            break

        prev = min(possible)

    print("YES" if ok else "NO")
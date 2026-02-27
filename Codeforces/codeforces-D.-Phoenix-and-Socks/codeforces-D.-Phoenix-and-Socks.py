# D. Phoenix and Socks
# Platform: Codeforces
from collections import Counter

for _ in range(int(input())):
    n, l, r = map(int, input().split())
    colors = list(map(int, input().split()))

    left = Counter(colors[:l])
    right = Counter(colors[l:])


    for c in list(left.keys()):
        m = min(left[c], right[c])
        left[c] -= m
        right[c] -= m
        if left[c] == 0:
            del left[c]
        if right[c] == 0:
            del right[c]

    L = sum(left.values())
    R = sum(right.values())

    if L < R:
        left, right = right, left
        L, R = R, L

    cost = 0
    diff = L - R
    for c in left:
        while left[c] >= 2 and diff > 0:
            left[c] -= 2
            diff -= 2
            cost += 1


    cost += diff // 2

    remaining = sum(left.values()) + sum(right.values())
    cost += remaining // 2

    print(cost)

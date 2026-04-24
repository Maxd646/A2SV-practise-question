import sys, math, heapq, itertools
from itertools import permutations, combinations, combinations_with_replacement
from itertools import product, accumulate, groupby, chain
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right, insort_left, insort_right, bisect, insort 
from functools import lru_cache

input = sys.stdin.readline
num = lambda: int(input())
number = lambda: map(int, input().split())
numbers = lambda: list(map(int, input().split()))
words = lambda: sys.stdin.readline().strip().split()
word = lambda: sys.stdin.readline().strip()
minn = float('inf')
maxx = float('-inf')
MOD = 10**9 + 7

YES = lambda: print('YES')
NO = lambda: print('NO')

#sys.setrecursionlimit(10**7)
@lru_cache(None)
def dp():
    pass

test_cases = lambda inp=0: num() if not inp else inp
def solve():
    n = num()
    arr = [num() for _ in range(n)]
    seen = defaultdict(list)
    roots =[]
    for i in range(n):
        if arr[i]==-1:
            roots.append(i)
        else:
            seen[arr[i]-1].append(i)
    q = deque([root, 1] for root in roots)
    maxx = 0
    while q:
        node, depth = q.popleft()
        maxx = max(maxx, depth)
       
        for child in seen[node]:
            q.append((child, depth+1))

    print(maxx)
    return

for _ in range(1):
    solve()
import sys, math, heapq, itertools
from itertools import permutations, combinations, combinations_with_replacement
from itertools import product, accumulate, groupby, chain
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
from functools import lru_cache

input = sys.stdin.readline
number = lambda: int(input())
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

test_cases = lambda inp=0: number() if not inp else inp
def solve():
    n = number()
    if n%2==0:
        print(*[i for i in range(n, 0, -1)])
    elif n==1 or n==3:
        print(-1)
    else:
        print(*[i for i in range(n//2+1, n+1)]+[i for i in range(n//2, 0, -1)])
        
    return

for _ in range(test_cases()):
    solve()
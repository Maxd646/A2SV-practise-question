import sys, math, heapq, itertools
from itertools import permutations, combinations, combinations_with_replacement
from itertools import product, accumulate, groupby, chain
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
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
    m = num()
    p = numbers()

    def dfs(l, r):
        if l == r:
            return 0, p[l], p[l]  
        
        mid = (l + r) // 2
        
        left, lmin, lmax = dfs(l, mid)
        right, rmin, rmax = dfs(mid + 1, r)
        
        if left == -1 or right == -1:
            return -1, 0, 0
        
       
        if lmax < rmin:
            return left + right, min(lmin, rmin), max(lmax, rmax)
        
        
        elif rmax < lmin:
            return left + right + 1, min(lmin, rmin), max(lmax, rmax)
        
      
        else:
            return -1, 0, 0

    ans, _, _ = dfs(0, m - 1)
    print(ans)
    
    return

for _ in range(test_cases()):
    solve()
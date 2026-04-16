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
    arr = list(word())
    n= len(arr)
    seen = set(arr)
    if len(set(arr))!=n: NO()
    elif "a" not in seen:
        NO()
    else:
        l = arr.index("a")
        r = l
        for i in range(1, n):
            ch = chr(ord("a")+i)
            if ch not in seen:
                NO()
                break
            pos = arr.index(ch)
            if pos != l-1 and pos != r+1:
                NO()
                break
            l= min(l, pos)
            r= max(r, pos)
        else:
            YES()
    return

for _ in range(test_cases()):
    solve()
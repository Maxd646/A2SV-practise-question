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
    s, y = input().split()
    if s==y:
        print("=")
    elif "S" in y and "S" in s:
        if len(s) < len(y):
            print(">")
        else:
            print("<")
    elif "L" in y and "L" in s:
        if len(s) < len(y):
            print("<")
        else:
            print(">")
    elif "L" in y or "L" in s:
        if "L" in y:
            print("<")
        else:
            print(">")
    elif "S" in y or "S" in s:
        if "S" in y:
            print(">")
        else:
            print("<")
    return

for _ in range(test_cases()):
    solve()
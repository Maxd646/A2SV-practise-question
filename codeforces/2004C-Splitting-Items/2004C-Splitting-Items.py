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
    arr = numbers()

    
def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    
    arr.sort(reverse=True)
    for i in range(1, n, 2):
        diff = arr[i-1] - arr[i]
        use = min(diff, k)
        arr[i] += use
        k -= use

    score = 0
    for i in range(n):
        if i % 2 == 0:
            score+= arr[i]
        else:
            score-= arr[i]

    print(max(0, score))


for _ in range(test_cases()):
    solve()
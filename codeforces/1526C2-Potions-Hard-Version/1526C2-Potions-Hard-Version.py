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
    heap = []
    ans = 0
    summ = 0
    summne = 0
    for i in range(n):
        if arr[i]>=0:
            summ+=arr[i]
            ans+=1
        else:
            heapq.heappush(heap, arr[i])
            summne+=arr[i]
            if summ<abs(summne):
                x = heapq.heappop(heap)
                summne-=x
    print(ans + len(heap))
    return
for _ in range(1):
    solve()
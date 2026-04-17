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
    a, b, c, m = map(int, input().split())

    A = m // a
    B = m // b
    C = m // c

    AB = m // math.lcm(a, b)
    AC = m // math.lcm(a, c)
    BC = m // math.lcm(b, c)
    ABC = m // math.lcm(a, b, c)

    oA = A - AB - AC + ABC
    oB = B - AB - BC + ABC
    oC = C - AC - BC + ABC

    oAB = AB - ABC
    oAC = AC - ABC
    oBC = BC - ABC

    totalA = oA*6 + oAB*3 + oAC*3 + ABC*2
    totalB = oB*6 + oAB*3 + oBC*3 + ABC*2
    totalC = oC*6 + oAC*3 + oBC*3 + ABC*2

    print(totalA, totalB, totalC)

    return
for _ in range(test_cases()):
    solve()
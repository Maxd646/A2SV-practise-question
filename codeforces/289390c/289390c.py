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
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.rank = [1] * (n+1)
        self.expre = [0]*(n+1)
    lru_cache(None)
    def find(self, u):
        if self.parent[u] != u:
            return self.find(self.parent[u])
        return u
    def union(self, u, v):
        px = self.find(u)
        py = self.find(v)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        self.expre[py] -= self.expre[px]
        self.rank[px] += self.rank[py]
        return True
    
def solve():
    n, m = number()
    union = UnionFind(n)
    arr = []
    for _ in range(m):
        arr = input().split()
        if arr[0] == "join":
                union.union(int(arr[1]), int(arr[2]))
        elif arr[0] == "add":
            union.expre[union.find(int(arr[1]))]+=int(arr[2])
        else:
            x = int(arr[1])
            ans = union.expre[int(arr[1])]
            while x != union.parent[x]:
                ans += union.expre[union.parent[x]]
                x = union.parent[x]
            print(ans)
    return
for _ in range(1):
    solve()
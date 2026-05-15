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
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        px = self.find(u)
        py = self.find(v)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        self.rank[px] += self.rank[py]
        return True
    
def solve():
    n, m, k  = number()
    union = UnionFind(n)
    arr = []
    for _ in range(m):
        input()
    for _ in range(k):
        a, b, c = input().split()
        b, c = int(b), int(c)
        arr.append((a, b, c))
    arr = arr[::-1]
    ans = []
    for a, b, c in arr:
        if a == "cut":
            union.union(b, c)
        else:
            if union.find(b) == union.find(c):
                ans.append("YES")
            else:
                ans.append("NO")
    print("\n".join(ans[::-1]))
    
    return
for _ in range(1):
    solve()
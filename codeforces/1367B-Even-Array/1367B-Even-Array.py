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
    even = [x for x in arr if x % 2 == 0]
    odd = [x for x in arr if x % 2 == 1]
    if not (len(even)==len(odd) or len(even)==len(odd)+1 or len(even)+1==len(odd)):
        print(-1)
        return
    arrr =[]
    i = 0
    while i<len(even) and i<len(odd):
        arrr.append(even[i])
        arrr.append(odd[i])
        i+=1
    if i<len(even):
        arrr.append(even[i])
    elif i<len(odd):
        arrr.append(odd[i])
    count= 0
    for i in range(len(arr)):
        if i%2==0:
            if arrr[i]%2==1:
                print(-1)
                return
            if arrr[i]%2==0 and arr[i]%2==0:
                continue
            else:
                count+=1
        else:
            if arrr[i]%2==0:
                print(-1)
                return
            if arrr[i]%2==1 and arr[i]%2==1:
                continue
            else:
                count+=1
    print(count//2)
    return

for _ in range(test_cases()):
    solve()
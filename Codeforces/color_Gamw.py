import sys
input = sys.stdin.readline

def binary(arr, x, left, right):
    while left < right:
        mid = (left + right) // 2
        
        if arr[mid] <= x:
            left = mid + 1
        else:
            right = mid
            
    return left

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    ans = 0

    for i in range(n):
        for j in range(i):
            
            x = max(a[n-1], 2*a[i]) - a[i] - a[j]
            
            k = binary(a, x, 0, j)
            
            ans += j - k

    print(ans)

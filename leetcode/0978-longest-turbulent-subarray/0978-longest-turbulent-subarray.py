class Solution:
    def maxTurbulenceSize(self, arr):
        n= len(arr)
        if n < 2:
            return n

        ans = 1
        anchor = 0

        c = 0
        d = 0
        for i in range(1, n):
            c = 1 if arr[i - 1] < arr[i] else 0 if arr[i - 1] == arr[i] else -1
            if i!= n-1:
                d =  1 if arr[i] < arr[i+1] else 0 if arr[i] == arr[i+1] else -1
            if c == 0:
                anchor = i
            else:
                if i == n - 1 or c * d != -1:
                    ans = max(ans, i - anchor + 1)
                    anchor = i
        return ans
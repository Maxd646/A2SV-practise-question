import bisect

class Solution:
    def findClosestElements(self, arr, k, x):
        right = bisect.bisect_left(arr, x)
        left = right - 1

        ans = []

        while len(ans) < k:

            if left < 0:
                ans.append(arr[right])
                right += 1

            elif right >= len(arr):
                ans.append(arr[left])
                left -= 1

            elif abs(arr[left] - x) <= abs(arr[right] - x):
                ans.append(arr[left])
                left -= 1

            else:
                ans.append(arr[right])
                right += 1

        return sorted(ans)
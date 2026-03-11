from collections import deque

class Solution:
    def minKBitFlips(self, nums, k):
        q = deque()
        ans = 0

        for i in range(len(nums)):
            while q and i > q[0] + k - 1:
                q.popleft()

            curr = nums[i] ^ (len(q) % 2)

            if curr == 0:
                if i + k > len(nums):
                    return -1
                ans += 1
                q.append(i)

        return ans
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        
        bucket = [[] for _ in range(len(nums)+1)]
        for num, val in count.items():
            bucket[val].append(num)

        ans = []
        
        for num in reversed(bucket):
            if num:
                ans.extend(num)
            if len(ans) == k:
                return ans
        return ans
        
        
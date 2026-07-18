class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        res = []
        total = sum(nums)
        zero = 0
        seen = Counter()
        for i in range(len(nums)):
            if i == 0:
                seen[i] = total
                if nums[i] ==0:
                    zero +=1
                else:
                    total -= 1
                continue
            seen[i] = total + zero
            total -= nums[i]
            if nums[i] ==0:
                zero +=1
        seen[len(nums)] = zero
        maxx = 0
        for j, num in seen.items():
            maxx = max(num, maxx)
        for i, num in seen.items():
            if num == maxx:
                res.append(i)
        return res
            
            


        
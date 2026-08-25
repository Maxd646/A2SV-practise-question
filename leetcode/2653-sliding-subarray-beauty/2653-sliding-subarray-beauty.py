class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:

        arr = SortedList(nums[:k])
        ans = []
        ans.append(min(arr[x-1], 0))

        for i in range(k, len(nums)):

            arr.remove(nums[i-k])
            arr.add(nums[i])
            ans.append(min(0, arr[x-1]))

        return ans

       


        

            



        



        
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:

        def find():

            count = 0

            for  i in range(102):

                count += seen[i]

                if count >= x:
                    return min(0, i-50)

            return 0

        seen = [0]*102
        ans  = []

        for i in range(k):

            seen[nums[i]+50] +=1

        ans.append(find())

        for j in range(k, len(nums)):

            seen[nums[j] + 50] += 1
            seen[nums[j-k]+50] -= 1
            ans.append(find())

        return ans



       


        

            



        



        
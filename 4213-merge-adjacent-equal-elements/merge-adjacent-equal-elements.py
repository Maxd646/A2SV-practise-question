class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:

        stack = []
        n = len(nums)

        for i in range(n):

            if stack and stack[-1] == nums[i]:

                val = stack.pop() + nums[i]

                while stack and stack[-1] == val:

                    val = stack.pop() + val

                stack.append(val)
                continue
            
            stack.append(nums[i])

        return stack
        
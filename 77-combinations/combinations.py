class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        nums = [num for num in range(1, n+1)]


        def backtrack(i, combination):
            if len(combination) == k:
                combinations.append(combination[:])
                return

            if i >= n:
                return
            
            backtrack(i+1, combination + [nums[i]])

            backtrack(i + 1, combination)

        combinations = []
        backtrack(0, [])
        return combinations


            
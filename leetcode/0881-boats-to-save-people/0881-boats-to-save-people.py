class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:

        people.sort()

        left, right = 0, len(people)-1
        ans = 0

        while left <= right:

            if people[right] >= limit or people[left] + people[right]> limit:
                ans += 1
                right -= 1
                
            elif people[left] + people[right] <= limit:

                ans += 1
                left += 1
                right -= 1
              
        return ans  
        
# Boats to Save People
# Platform: LeetCode
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        if all(num>=limit for num in people):
            return len(people)
        left, right=0, len(people)-1
        ans=0
        while left<right:
            if people[left]+people[right]>limit and left+1==right:
                ans+=2
                break
            elif  people[left]+people[right]<=limit and left+2==right:
                ans+=2
                break
            elif people[left]+people[right]>limit:
                ans+=1
                right-=1
            else:
                ans+=1
                left+=1
                right-=1
        return ans

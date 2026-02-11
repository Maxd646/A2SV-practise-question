# Find the Most Common Response
# Platform: LeetCode
class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        seen=set()
        result=[]
        for ch in responses:
            seen.clear()
            for word in ch:
                if word not in seen:
                    seen.add(word)
                    result.append(word)
        count=Counter(result)
        return sorted(count.items(), key=lambda x: (-x[1], x[0]))[0][0]

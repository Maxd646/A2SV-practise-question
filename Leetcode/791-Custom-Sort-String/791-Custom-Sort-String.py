# Custom Sort String
# Platform: LeetCode
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count= Counter(s)
        seen= set(s)
        result=[]
        need=Counter(s)-Counter(result)
        for i in range(len(order)):
            if order[i] in seen:
                for j in range(count[order[i]]):
                    result.append(order[i])
        
        extra=count-Counter(result)
        return "".join(result)+ "".join(ch*num for ch, num in extra.items())

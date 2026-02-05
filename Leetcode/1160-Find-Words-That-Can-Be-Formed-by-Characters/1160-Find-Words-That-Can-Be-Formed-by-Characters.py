# Find Words That Can Be Formed by Characters
# Platform: LeetCode
from collections import Counter
class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        seen=Counter(chars)
        result=0
        for ch in words:
            found =True
            seen2=Counter(ch)
            for i in range(len(ch)):
                if ch[i] not in seen or seen2[ch[i]]>seen[ch[i]]:
                    found=False
                    break
            if found:
                result+=len(ch)
        return result


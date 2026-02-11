# Sort Characters By Frequency
# Platform: LeetCode

class Solution:
    def frequencySort(self, s: str) -> str:
        count= Counter(s)
        result= [ch*num for ch, num in sorted(count.items(), key=lambda x:x[1], reverse= True)]
        return "".join(result)


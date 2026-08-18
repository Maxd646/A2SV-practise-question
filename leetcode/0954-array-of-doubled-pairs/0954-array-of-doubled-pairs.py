class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:

        arr.sort(key=abs)
        count = Counter(arr)
        n = len(arr) // 2

        x = 0
        if arr.count(0)%2!= 0:
            return False
            
        for num in arr:
            if count[num] > 0 and count[num * 2] > 0:
                x += 1
                count[num * 2] -= 1
                count[num] -= 1

        return x == n
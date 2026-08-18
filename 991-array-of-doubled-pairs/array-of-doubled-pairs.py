class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:

        arr.sort(key = abs)
        count = Counter(arr)
        
        for num in arr:
            if count[num] ==0 :
                continue 
            if count[num*2] == 0:
                return False
            
            count[num] -= 1
            count[num*2] -= 1

        return True






        



        
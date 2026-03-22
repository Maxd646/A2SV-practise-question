class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        if k==0:
            return len(set(arr))
        seen= sorted(Counter(arr).items(), key= lambda x:x[1])
        total= len(seen)
        for key, val in seen:
            if k>=val:
                total-=1
                k-=val
            else:
                break
        return total

            

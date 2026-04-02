class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        def binary(heaters, house):

            def binarysearch (left, right, minn):

                if left>right:
                    return minn

                mid = left + (right -left)//2
                minn  = min(minn, abs(heaters[mid]-house))

                if heaters[mid]>house:
                    return binarysearch(left, mid-1, minn)

                else: return binarysearch(mid+1, right, minn)

            return binarysearch(0, len(heaters)-1, float("inf"))
        
        radius = 0
        for house in houses:

            radius = max(radius, binary(heaters, house))
        return radius
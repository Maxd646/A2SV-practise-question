class Solution:
    def createSortedArray(self, ins: List[int]) -> int:
        heap = []
        ans = 0
        for item in ins:
            l = bisect_left(heap, item)
            r = len(heap)-bisect_right(heap, item)
            ans+= min(l, r)
            insort(heap, item)
        return ans % (10 **9 + 7)

        
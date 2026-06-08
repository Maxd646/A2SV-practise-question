class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        for num in nums:
            if num>0:
                pos.append(num)
            else:
                neg.append(num)
        return [x for x in itertools.chain(*zip(pos, neg))]
        
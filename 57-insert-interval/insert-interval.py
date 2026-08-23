class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        left , right = [], []

        start, end = newInterval

        for interval in intervals:
            
            if interval[1] <start:
                left.append(interval)
            
            elif interval[0] > end:
                right.append(interval)

            else:

                start = min(interval[0], start)
                end = max(interval[1], end)


        return left + [[start, end]] + right
        

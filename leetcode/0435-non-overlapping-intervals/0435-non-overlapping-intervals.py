class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort()

        end = intervals[0][1]

        count = 0

        for start, final in intervals[1:]:

            if start < end:
                count += 1
                end = min(end, final)
            else:
                end = max(final, end)

        print(intervals)

        return count




        
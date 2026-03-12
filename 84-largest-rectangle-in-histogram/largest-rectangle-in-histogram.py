class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        area=0
        for i, h in enumerate(heights):
            j=i
            while stack and stack[-1][1]>h:
                index, hi=stack.pop()
                area=max(area, hi*(i-index))
                j=index
            stack.append((j, h))
        for i, h in stack:
            area = max(area, h*(len(heights)-i))

        return area
        
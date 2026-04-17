class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        seen =set()
        for ch, num in edges:
            if ch in seen:
                return ch
            elif num in seen:
                return num
            seen.add(ch)
            seen.add(num)
            
        
        
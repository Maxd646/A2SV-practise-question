class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        left = 0
        for i in range(len(pushed)):
            stack.append(pushed[i])
            while stack and  stack[-1] == popped[left]:
                stack.pop()
                left+=1

        if left<len(popped)-1:
            while stack and stack[-1] == popped[left] and left <len(popped):
                stack.pop()
                left+=1  
                
        if stack:return False
        return True
            
            



       
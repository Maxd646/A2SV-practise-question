class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack=[]
        for star in asteroids:
            while stack and star<0 and stack[-1]>0:
                if stack[-1]<-star:
                    stack.pop()
                    continue
                elif stack[-1]==-star:
                    stack.pop()
                break
            else:
                stack.append(star)
        return stack
           

       
                    



        
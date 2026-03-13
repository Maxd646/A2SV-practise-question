class Solution:
    def splitNum(self, num: int) -> int:
        num = list(map(int, str(num)))
        num.sort()
        num1=0
        num2=0
        for i in range(len(num)):
            if i%2==0:
                num1=10*num1+num[i]
            else:
                num2=10*num2+num[i]
        return num1+num2


\
        




        
        
        
      
        
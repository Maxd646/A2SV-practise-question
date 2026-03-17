class Solution:
    def myPow(self, x: float, n: int) -> float:
        b=n
        if n<0:
            n=-n

        def  name(x, n):
            print('state', x, n)
            if n<=0:
                print('res', 1)
                return 1

            a=name(x, n//2)
            if n%2==0:
                print('res', a*a)
                return a*a
            else:
                print('res', x*a*a)
                return x*a*a
        if b>=0:
            return  name(x, n)     
        else:
            return 1/name(x, n) 
        

        
        
        
       
        
        
    

       
        
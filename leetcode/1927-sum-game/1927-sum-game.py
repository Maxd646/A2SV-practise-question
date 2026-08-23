class Solution:
    def sumGame(self, num: str) -> bool:


        n = len(num)//2

        suml = sum(int(num[i]) for i in range(n) if num[i] != "?")
        sumr = sum(int(num[i]) for i in range(n, len(num)) if num[i] != "?")

        nl = num[:n].count("?")
        nr = num[n:].count("?")

        diffq = nl - nr 
        diff = suml - sumr

        if diffq ==0:
            return diff!= 0
        return diff != -9 * diffq / 2
        
        
       

            
        
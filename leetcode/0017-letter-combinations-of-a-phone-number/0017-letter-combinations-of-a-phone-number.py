from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        digit = {"2":["a", "b", "c"], "3":["d", "e", "f"], "4":["g", "h", "i"], "5":["j", "k", "l"], "6":["m", "n", "o"], "7":["p", "q", "r", "s"], "8":["t", "u", "v"], "9":["w", "x", "y", "z"]}

        if len(digits) == 1:
            return digit[digits[0]]

        elif len(digits) == 2:
            for i in range(len(digit[digits[0]])):
                for j in range(len(digit[digits[1]])):
                    ans.append(digit[digits[0]][i] + digit[digits[1]][j])
            return ans

        elif len(digits) == 3:
            for i in range(len(digit[digits[0]])):
                for j in range(len(digit[digits[1]])):
                    for k in range(len(digit[digits[2]])):
                        ans.append(digit[digits[0]][i] + digit[digits[1]][j] + digit[digits[2]][k])
            return ans

        else:
            for i in range(len(digit[digits[0]])):
                for j in range(len(digit[digits[1]])):
                    for k in range(len(digit[digits[2]])):
                        for m in range(len(digit[digits[3]])):
                            ans.append(digit[digits[0]][i] + digit[digits[1]][j] + digit[digits[2]][k] + digit[digits[3]][m])
            return ans
            

            
        
        
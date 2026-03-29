class Solution:
    def splitString(self, s: str) -> bool:
        current = []
        def backtrack(j):
            if j >= len(s):
                return len(current) >= 2
            print(j)
            for i in range(j, len(s)):
                val = int(s[j:i+1])
                print(val)
                if len(current) == 0 or val == current[-1] - 1:
                    current.append(val)
                    print(current)
                    if backtrack(i + 1):
                        print("yes")
                        return True
                    current.pop()
            return False
        return backtrack(0)
        
        
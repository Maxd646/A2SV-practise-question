class Solution:
    def longestPalindrome(self, s: str) -> str:

        ans = ""
        n = len(s)

        queue = deque()
        
        for i in range(n):

            left, right = i, i

            while left >= 0 and right < n and s[left] == s[right]:
                
                if left == right:
                    queue.appendleft(s[left])
                else:
                    queue.appendleft(s[left])   
                    queue.append(s[right])
                left -= 1
                right += 1

            temp = "".join(list(queue))

            queue = deque()
            
            if len(ans) < len(temp):

                ans = temp

            left, right = i, i+1

            while left >= 0 and right < n and s[left] == s[right]:

                queue.appendleft(s[left])
                queue.append(s[right])
                left -= 1
                right += 1

            temp = "".join(list(queue))

            if len(ans) < len(temp):
                ans = temp
            
            queue = deque()

        return ans





            

            
            
        
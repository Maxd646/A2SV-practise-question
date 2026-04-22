from collections import deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        seen = set(wordList)
        if endWord not in seen:
            return 0

        queue = deque([(beginWord, 1)])

        while queue:
            word, s = queue.popleft()

            if word == endWord:
                return s

            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    newWord = word[:i] + c + word[i+1:]
                    
                    if newWord in seen:
                        queue.append((newWord, s + 1))
                        seen.remove(newWord)  

        return 0
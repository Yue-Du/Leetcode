from typing import List
class Solution:
    def findString(self, words: List[str], s: str) -> int:
        for i in range(len(words)):
            if words[i] == s:
                return i

        return -1

New = Solution()
New.findString(["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""], "ball")
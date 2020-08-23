from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        if s==[]:
            return []
        i=1
        while i <len(s)+1:
            s.insert(-i,s[0])
            s.pop(0)
            i=i+1
        s.insert(0,s[-1])
        s.pop()
        return s


New = Solution()
New.reverseString(["h","e","l","l","o"])
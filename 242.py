class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        news = sorted(list(s))
        newt = sorted(list(t))
        if news == newt:
            return True
        else:
            return False


New = Solution()
New.isAnagram('av','ba')
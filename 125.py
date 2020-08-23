class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ''
        for i in s:
            if i.isalpha() or i.isdigit():
                new += i
        new = new.lower()
        b = new[::-1]
        if new == b:
            return True
        else:
            return False


New = Solution()
New.isPalindrome("A man, a plan, a canal: Panama")
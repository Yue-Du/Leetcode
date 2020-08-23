class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)
        half = length // 2
        i=1
        while i <= half:
            substr = s[:i]
            if length % i == 0:
                j=0
                while j+i <= length:
                    if substr != s[j:j+i]:
                        break
                    else:
                        j = j+i
                if j ==length:
                    return True
            i+=1
        return False

New = Solution()
New.repeatedSubstringPattern("ababababab")
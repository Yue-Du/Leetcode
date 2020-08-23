class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hay = list(haystack)
        nee = list(needle)
        if haystack == "":
            return 0
        if len(hay) < len(nee):
            return -1
        for i in range(len(hay)):
            if hay[i:i+len(nee)] == nee:
                return i
        return -1


New = Solution()
New.strStr("hello","ll")
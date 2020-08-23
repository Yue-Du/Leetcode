class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=1
        j=0
        max_len=0
        while j <len(s):
            while i <= len(s):
                if len(set(s[j:i]))==len(s[j:i]):
                    if len(s[j:i])> max_len:
                        max_len = len(s[j:i])
                    i=i+1
                else:
                    j=j+1
                    i=j+1
            else:
                break
        return max_len


New = Solution()
New.lengthOfLongestSubstring("abcabcbb")
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashtable = {}
        i = 0
        j = 0
        res = 0
        cnt = 0
        while j < len(s):
            if s[j] not in hashtable or hashtable[s[j]] == 0:
                hashtable[s[j]] = 1
                j += 1
                cnt += 1
                res = max(cnt, res)
            else:
                hashtable[s[i]] = 0
                i += 1
                cnt -= 1

        return res


New = Solution()
New.lengthOfLongestSubstring("abcabcbb")
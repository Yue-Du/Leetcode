import copy
class Solution(object):
    def permutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        length = len(S)

        def helper(s, res, temp):
            if len(temp) == length:
                dcopy = copy.deepcopy(temp)
                return res.append(dcopy)
            for i in range(len(s)):
                if i>0 and s[i] == s[i - 1]:
                    continue
                temp = temp + s[i]
                helper(s[:i] + s[i + 1:], res, temp)
                temp = temp[:-1]
            return res

        return helper(sorted(S), [], '')


New = Solution()
New.permutation('qqe')
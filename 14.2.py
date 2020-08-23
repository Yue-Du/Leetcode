from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs==[]:
            return ""
        h = 0
        new_len = (len(strs) - 1)
        ind_ex=0
        while h < new_len:
            if len(strs[h]) > len(strs[h + 1]):
                ind_ex = h + 1
            else:
                ind_ex = h
            h = h + 1
        j = 0
        prefix = ""
        flag = False
        while j < len(strs[ind_ex]):
            i = 1
            while i <= new_len:
                if strs[0][j] == strs[i][j]:
                    i = i + 1
                else:
                    print(prefix)
                    flag = True
                    break
            if flag:
                break
            prefix += strs[0][j]
            j = j + 1
        if not flag:
            print(prefix)
case = Solution()
case.longestCommonPrefix([])


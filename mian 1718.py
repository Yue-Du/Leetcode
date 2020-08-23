from typing import List
class Solution:
    def shortestSeq(self, big: List[int], small: List[int]) -> List[int]:
        small_size = len(small)
        small_map = {}
        for i in small:
            if i not in small_map:
                small_map[i] = 0
        l = 0
        r = 0
        cnt = 0
        res = [0,len(big)]
        while r < len(big):
            if big[r] not in small_map:
                r += 1
            else:
                small_map[big[r]] +=1
                if small_map[big[r]] ==1:
                    cnt += 1
                r+=1
            if cnt == small_size:
                if r-1-l<(res[1] - res[0]):
                    res[0] = l
                    res[1] = r-1
            while l< r:
                if big[l] not in small_map:
                    l+=1
                    if cnt==small_size:
                        res[0] = l
                elif cnt == small_size:
                    small_map[big[l]] -= 1
                    if small_map[big[l]] == 0:
                        cnt -=1
                    l+=1
                    if cnt == small_size:
                        res[0] = l
                else:
                    break
        if res[1] == len(big):
            return []
        else:
            return res


New = Solution()
New.shortestSeq([7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7],[1, 5, 9])
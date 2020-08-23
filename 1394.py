from typing import List
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        if len(arr) == 1 and arr[0] == 1:
            return 1
        elif len(arr) == 1:
            return -1
        new_arr = sorted(arr, reverse = True)
        i = 1
        cnt = 1
        while i < len(new_arr):
            if new_arr[i] == new_arr[i-1]:
                cnt += 1
            else:
                if cnt == new_arr[i-1]:
                    return new_arr[i-1]
                else:
                    cnt = 1
            i += 1
        return -1

New = Solution()
New.longestOnes([1,1,1,0,0,0,1,1,1,1,0],2)
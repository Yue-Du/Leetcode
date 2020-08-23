from typing import List
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        new_arr = sorted(arr)
        i = 0
        res = []
        mindiff = float('inf')
        while i < len(new_arr)-1:
            if new_arr[i] - new_arr[i-1] < mindiff:
                mindiff = new_arr[i] - new_arr[i-1]
                res = [[new_arr[i-1],new_arr[i]]]
            elif new_arr[i] - new_arr[i-1] == mindiff:
                res.append([new_arr[i-1],new_arr[i]])
            i += 1
        return res

New = Solution()
New.minimumAbsDifference([4,2,1,3])
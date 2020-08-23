from typing import List
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = 0
        for i in range(k):
            res = res + nums[k]
        res /= k
        cur = res
        for j in range(1,len(nums)-k+1):
            cur = (cur * k - nums[j-1] + nums[j+k-1]) / k
            res = max(res, cur)
        return res


New = Solution()
New.findMaxAverage([1,12,-5,-6,50,3],4)
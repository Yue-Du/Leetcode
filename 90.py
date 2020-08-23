import copy
from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        def helper(nums, index, res, temp):
            if index == len(nums):
                if temp not in res:
                    dcopy = copy.deepcopy(temp)
                    return res.append(dcopy)
                else:
                    return res
            temp.append(nums[index])
            helper(nums, index + 1, res, temp)
            temp.pop()
            helper(nums, index + 1, res, temp)
            return res

        return helper(nums, 0, [], [])


New = Solution()
New.subsetsWithDup([1,2,2])
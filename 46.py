import copy
from typing import List
class Solution:
   def permute(self, nums: List[int]) -> List[List[int]]:
        '''def backtrack(combination, nextnums):
            if len(nextnums)==0:
                return res.append(combination)
            else:
                for number in nextnums:
                    if number not in combination:
                        combination.append(number)
                        backtrack(combination, nextnums.remove(number), res)
                        combination.pop()
        res=[]
        backtrack([],nums)
        return res'''
        length = len(nums)
        def helper(nums, res, index, temp):
            if index == length:
                dcopy = copy.deepcopy(temp)
                return res.append(dcopy)
            for i in range(len(nums)):
                temp.append(nums[i])
                helper(nums[:i] + nums[i + 1:len(nums)], res, index + 1, temp)
                temp.pop()
            return res

        return helper(nums, [], 0, [])


New = Solution()
New.permute([1,2,3])
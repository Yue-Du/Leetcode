from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new = set(nums)
        if len(new) == len(nums):
            return False
        else:
            return True

        '''new = set(nums)
        for i in new:
            times = nums.count(i)
            if times > 1:
                return True
        return False'''

    '''i=0
    j=1
    while i < len(nums)-1:
        while j < len(nums):
            if nums[i]==nums[j]:
                return True
            else:
                j=j+1
        i=i+1
        j=i+1
    return False'''
from typing import List
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        i=0
        if k<len(nums):
            while i < len(nums)-k:
                j=i+1
                while j <= i+k:
                    if abs(nums[i]-nums[j])<=t:
                        return True
                    j=j+1
                i=i+1
        else:
            while i < len(nums)-1:
                j=i+1
                while j <len(nums):
                    if abs(nums[i]-nums[j])<=t:
                        return True
                    j=j+1
                i=i+1
        return False


New = Solution()
New.containsNearbyAlmostDuplicate([7,1,3],2,3)
from typing import List
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        new=set(nums)
        if len(new)>2:
            new.remove(max(new))
            new.remove(max(new))
            return max(new)
        elif len(new)>0:
            return max(new)
        else:
            return None


New = Solution()
New.thirdMax([2,1])
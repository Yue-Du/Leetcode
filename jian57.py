from typing import List
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        nums = [i for i in range(1,target)]
        left = 0
        right = 0
        res = []
        summ = nums[0]
        while right < len(nums):
            if summ == target:
                res.append(nums[left:right + 1])
                summ -= nums[left]
                left += 1
            elif summ > target:
                summ -= nums[left]
                left += 1
            else:
                right += 1
                summ += nums[right]
        return res

New = Solution()
New.findContinuousSequence(9)
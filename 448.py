from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        '''i=1
        max_num = len(nums)
        if nums == []:
            return []
        while i <=max(nums):
            if i in nums:
                nums.remove(i)
                if i in nums:
                    nums.remove(i)
                i=i+1
            else:
                nums.append(i)
                i=i+1
        return nums'''
        i = 0
        '''while i < len(nums):
            nums[nums[i] - 1] = -1 * nums[nums[i] - 1]
            i = i + 1'''
        for i in nums:
            nums[abs(i)-1]=-1*abs(nums[abs(i)-1])
        j = 0
        output = []
        while j < len(nums):
            if nums[j] > 0:
                output.append(j + 1)
            j = j + 1
        return output


New = Solution()
New.findDisappearedNumbers([4,3,2,7,8,2,3,1])
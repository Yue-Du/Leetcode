from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums)==0:
            return -1
        left=0
        right=len(nums)-1
        med=(left+right)//2
        while left+1 < right:
            if nums[med] > nums[right]:
                left=med
                med=(left+right)//2
            elif nums[med]<nums[right]:
                right=med
                med=(left+right)//2
        if nums[left]<nums[right]:
            zz=right
        else:
            zz=left
        if target==nums[zz]:
            return zz
        elif target<nums[0]:
            left=zz
            right=len(nums)-1
        else:
            left=0
            right=zz
        med=(left+right)//2
        while left+1 < right:
            if nums[med]<target:
                left=med
                med=(left+right)//2
            else:
                right=med
                med=(left+right)//2
        if nums[left]==target:
            return left
        elif nums[right]==target:
            return right
        else:
            return -1


New = Solution()
New.search([1,3,5],5)
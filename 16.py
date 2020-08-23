from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        k=0
        nums_sort=sorted(nums)
        dist=abs(target)+(len(nums)*(abs(min(nums))+max(nums))/2)
        output=0
        while k <len(nums_sort)-2:
            i=k+1
            while i<len(nums_sort)-1:
                j = len(nums_sort) - 1
                while i<j:
                    if abs(nums_sort[k] + nums_sort[i] + nums_sort[j] - target) <= dist:
                        dist = abs(nums_sort[k] + nums_sort[i] + nums_sort[j] - target)
                        output = nums_sort[k] + nums_sort[i] + nums_sort[j]
                        j = j - 1
                        while i < j and nums_sort[j] == nums_sort[j + 1]:
                            j = j - 1
                    else:
                        j = j - 1
                        while i < j and nums_sort[j] == nums_sort[j + 1]:
                            j = j - 1
                i=i+1
                while i<len(nums_sort)-1 and nums_sort[i] == nums_sort[i - 1]:
                    i=i+1
            k=k+1
            while k <len(nums_sort)-2 and nums_sort[k]==nums_sort[k-1]:
                k=k+1
        return output


New = Solution()
New.threeSumClosest([0,2,1,-3],1)
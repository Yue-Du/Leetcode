from typing import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        while i < n:
            if j < m:
                if nums2[i] <= nums1[j]:
                    nums1.insert(j, nums2[i])
                    m = m + 1
                    i = i + 1
                    j = j+1
                j=j+1
            else:
                nums1.insert(j,nums2[i])
                j=j+1
                i=i+1
        return nums1

New = Solution()
New.merge([4,5,6,0,0,0],3,[1,2,3],3)
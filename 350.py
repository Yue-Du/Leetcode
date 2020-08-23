from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ss = list([])
        s = set(nums1) & set(nums2)
        while len(s) > 0:
            for i in s:
                nums1.remove(i)
                nums2.remove(i)
                ss.append(i)
            s = set(nums1) and set(nums2)
        return ss


New = Solution()
New.intersect([4,9,5],[9,4,9,8,4])
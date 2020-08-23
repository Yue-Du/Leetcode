from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        pre=nums[0]
        res=[]
        i=1
        while i <len(nums):
            if nums[i]!=nums[i-1]+1:
                if pre==nums[i]:
                    res.append('%s' % pre)
                else:
                    res.append("%s->%s"%(pre,nums[i-1]))
                pre = nums[i]
                i=i+1
            else:
                i=i+1
        if pre==nums[-1]:
            res.append('%s' % pre)
        if pre < nums[-1]:
            res.append("%s->%s" % (pre, nums[-1]))

        return res


New = Solution()
New.summaryRanges([0,1,2,4,5,7])
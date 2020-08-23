from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        mod1=nums[0]
        cnt1=0
        mod2=nums[0]
        cnt2=0
        i=0
        while i < len(nums):
            if nums[i]==mod1:
                cnt1=cnt1+1
            elif nums[i]==mod2:
                cnt2=cnt2+1
            else:
                if cnt1==0:
                    mod1=nums[i]
                    cnt1=1
                elif cnt2==0:
                    mod2=nums[i]
                    cnt2=1
                else:
                    cnt1=cnt1-1
                    cnt2=cnt2-1
            i=i+1
        j=0
        cnt1=0
        cnt2=1
        while j < len(nums):
            if nums[j]==mod1:
                cnt1=cnt1+1
            elif nums[j]==mod2:
                cnt2=cnt2+1
            j=j+1
        res=[]
        if cnt1>len(nums)/3:
            res.append(mod1)
        if cnt2>len(nums)/3:
            res.append(mod2)
        return res

New = Solution()
New.majorityElement([3,2,3])
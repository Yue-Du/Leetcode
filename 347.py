from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashtable = {}
        i = 0
        while i < len(nums):
            if nums[i] not in hashtable:
                hashtable[nums[i]] = 1
            else:
                hashtable[nums[i]] += 1
            i += 1
        count = sorted(hashtable.items(),key = lambda hashtable:hashtable[1],reverse = True)

        res = []
        for j in range(k):
            res.append(count[j][0])
        return res


New = Solution()
New.topKFrequent([2,2,3,1,1,1],2)
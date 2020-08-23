from typing import List
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        res=2
        i=1
        while i < len(timeSeries):
            for j in range(1,duration):
                if timeSeries[i] - timeSeries[i-1] > duration-j:
                    res+=duration - (j-1)
                    break
            i+=1
        return res


New = Solution()
New.findPoisonedDuration([1,2],2)
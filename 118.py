from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==0:
            return []
        if numRows==1:
            return [[1]]
        if numRows==2:
            return [[1],[1,1]]
        Trangle=[[]for i in range(numRows)]
        Trangle[0].append(1)
        Trangle[1].append(1)
        Trangle[1].append(1)
        i=2
        while i < numRows:
            j=0
            Trangle[i].append(1)
            while j < len(Trangle[i-2]):
                Trangle[i].append(Trangle[i-1][j]+Trangle[i-1][j+1])
                j=j+1
            Trangle[i].append(1)
            i=i+1
        return Trangle
New = Solution()
New.generate(3)
from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        target=n*n
        #res=[[0]*n]*n
        res = [[0 for _ in range(n)] for _ in range(n)]
        left=0
        right=n-1
        low=n-1
        high=0
        num=1
        while num < target:
            for i in range(left,right+1):
                res[high][i]=num
                num+=1
            high+=1
            for i in range(high, low+1):
                res[i][right]=num
                num+=1
            right-=1
            for i in range(right, left-1,-1):
                res[low][i]=num
                num+=1
            low-=1
            for i in range(low, high-1,-1):
                res[i][left]=num
                num+=1
            left+=1
        return res


New = Solution()
New.generateMatrix(3)
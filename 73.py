from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        i=0
        temp=[[],[]]
        while i < len(matrix):
            j=0
            while j < len(matrix[i]):
                if matrix[i][j]==0:
                    temp[0].append(i)
                    temp[1].append(j)
                j=j+1
            i=i+1
        row=set(temp[0])
        col=set(temp[1])
        for r in row:
            k=0
            while k < len(matrix):
                matrix[r][k]=0
                k=k+1
        for c in col:
            t=0
            while t < len(matrix):
                matrix[t][c]=0
                t=t+1
        return matrix

New = Solution()
New.setZeroes([[0,1]])
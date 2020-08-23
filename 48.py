from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix[0])
        for i in range(n):
            for j in range(n):
                temp=matrix[i][j]
                matrix[i][j]=matrix[j][i]
                matrix[j][i]=temp
        '''k=0
        l=len(matrix[0])-1
        while k<l:
            med=matrix[:,k]
            matrix[:,k] = matrix[:,l]
            matrix[:,l]=med
            k=k+1
            l=l-1'''
        for k in range(n):
            matrix[k].reverse()
        return matrix

New = Solution()
New.rotate([[1,2,3],[4,5,6],[7,8,9]])
from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        col = len(matrix[0])

        def helper(matrix, offset, size, res):
            if size == 1:
                res.append(matrix[0 + offset][0 + offset])
                return res

            for i in range(size - 1):
                res.append(matrix[0 + offset][i + offset])
            for i in range(size - 1):
                res.append(matrix[i + offset][col - 1 - offset])
            for i in range(size - 1):
                res.append(matrix[row - 1 - offset][col - 1 - i - offset])
            for i in range(size - 1):
                res.append(matrix[row - 1 - i - offset][0+offset])
            helper(matrix, offset + 1, size - 2, res)
            return res

        return helper(matrix, 0, len(matrix), [])


New = Solution()
New.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
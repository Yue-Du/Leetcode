from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        NROW=len(matrix)
        NCOL=len(matrix[0])
        def helper(depth):
            nrow=NROW-2*depth
            ncol=NCOL-2*depth
            if nrow<=0 or ncol<=0:
                return[]
            elif nrow==1:
                return matrix[depth][depth:depth+ncol]
            elif ncol==1:
                return [matrix[r][depth] for r in range(depth,depth+nrow)]

            res=[]
            res.append(matrix[depth][depth:depth+ncol-1])
            res.append([matrix[r][depth+ncol-1] for r in range(depth, depth+nrow-1)])
            low=matrix[depth+nrow-1][depth+1:depth+ncol]
            res.append(reversed(low))
            left=[matrix[r][depth] for r in range(depth+1,depth+nrow)]
            res.append(reversed(left))

            return res.append(helper(depth+1))
        return helper(0)


New = Solution()
New.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
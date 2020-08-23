# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        res=[]
        def helper(node,sum,temp):
            if not node:
                return
            sum =sum-node.val
            if not node.left and not node.right:
                if sum ==0:
                    temp.append(node.val)
                    res.append(temp)
                    return
            return helper(node.left,sum,temp+[node.val]) or helper(node.right,sum,temp+[node.val])

        helper(root,sum,[])
        return res


New = Solution()
New.pathSum([5,4,8,11,None,13,4,7,2,None,None,5,1],22)
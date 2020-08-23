from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def helper(node, res):
            if not node:
                return res
            helper(node.left,res)
            helper(node.right,res)
            res.append(node.val)
        return helper(root,[])



solution = Solution()
root = TreeNode(1)
root.left = None
root.right = TreeNode(2)
root.right.left = TreeNode(3)
root.right.right = None

solution.postorderTraversal(root)
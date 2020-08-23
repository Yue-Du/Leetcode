# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def mirrorTree(root):
            if not root:
                return
            temp = root.left
            root.left = root.right
            root.right = temp
            mirrorTree(root.left)
            mirrorTree(root.right)
            return root

        def issame(node1, node2):
            if not node1 and not node2:
                return True
            elif not node1 or not node2 or node1.val != node2.val:
                return False
            return issame(node1.left, node2.left) and issame(node1.right, node2.right)

        mirror = mirrorTree(root)
        return issame(root, mirror)


solution = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = None
root.left.right = TreeNode(3)
root.right.left = None
root.right.right = TreeNode(3)

solution.isSymmetric(root)

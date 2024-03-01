# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        s = 0

        def range(root):
            nonlocal s
            if root:
                if (low <= root.val <= high):
                    s += root.val
                    
                range(root.left)
                range(root.right)
        range(root)
        return s
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = 0

        def traverse(root):
            nonlocal ans, k
            if root:
                traverse(root.left)
                k -= 1
                if k == 0:
                    ans = root.val
                traverse(root.right)
     
        traverse(root)
        return ans
        
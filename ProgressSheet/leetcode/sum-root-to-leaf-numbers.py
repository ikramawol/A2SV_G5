# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        s = 0
        def rootToLeaf(root, s):
            nonlocal ans
            if root:
                s += root.val

                if root.left == None and root.right == None:
                    ans += s
                    return ans
                else:
                    rootToLeaf(root.left, s*10)
                    rootToLeaf(root.right, s*10)
                    
        rootToLeaf(root, s)
        return ans
          
                
        
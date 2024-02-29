# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = []
        # left child -> parent -> right child
        def inorder(root):
            if root:
                inorder(root.left)
                ans.append(root.val)
                inorder(root.right)
           
        inorder(root)
        
        for i in range(len(ans)-1):
            if ans[i] >= ans[i+1]:
                return False
                break
        else:
            return True
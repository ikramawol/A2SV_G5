# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
       
        _max = root.val
        _min = root.val
        def ansistor(root,_max, _min):
            if not root:
                return 0
            
            if root.val > _max:
                _max = root.val
            elif root.val < _min:
                _min = root.val
            
         
            left = ansistor(root.left, _max, _min)
            
            right = ansistor(root.right, _max, _min)
            
            
            return max(_max - _min, left, right)

        return ansistor(root, _max, _min)
        
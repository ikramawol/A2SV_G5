# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        
        def makeBST(l, r):

            if l == r:
                return TreeNode(nums[l])

            if l > r:
                return
            mid = (l+r)//2
            root = TreeNode(nums[mid])
            leftSide = makeBST(l, mid - 1)
            rightSide = makeBST(mid + 1, r)

            root.left = leftSide
            root.right = rightSide

            return root
            
        return makeBST(0, len(nums)-1)
        
        

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Find the indorder successor
        def minValueNode(node):
            current = node

            # Find the leftmost leaf
            while current.left:
                current = current.left
        
            return current
        
        if root == None:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            # If the node is with only one child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            # If the node have 2 child
            # place the inorder successor in posision of the node to be deleted 
            temp = minValueNode(root.right)
            root.val = temp.val

            # delete the inorder successor
            root.right = self.deleteNode(root.right, temp.val)

        return root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        ans =[]
        count = defaultdict(int)

        def counter(root):
            if root:
                count[root.val] += 1
                counter(root.left)
                counter(root.right)

        counter(root)
        _max = max(count.values())

        print(_max)

        for i in count:
            if count[i] == _max:
                ans.append(i)
        return ans

             

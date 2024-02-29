# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = defaultdict(list)
        level = 0
        def zigzag(root,level):
            nonlocal dic
            if root:
                dic[level].append(root.val)
                level += 1
                # if level % 2 != 0:
                #     zigzag(root.right, level)
                #     zigzag(root.left, level)
                # else:
                zigzag(root.left, level)
                zigzag(root.right, level)
            
        zigzag(root,level)
        ans = []
        print(dic)
        for i in dic:
            if i % 2 == 0:
                ans.append(dic[i])
            else:
                dic[i].reverse()
                ans.append(dic[i])
        return ans

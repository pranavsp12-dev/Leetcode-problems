# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d=0
        def height(node):
            nonlocal d  #we declared d=0 outiside the function so it avoids it becoming a new variable
            if node is None:
                return 0
            left=height(node.left)
            right=height(node.right)
            d=max(d,left+right)
            h=max(left,right)+1
            return h
        height(root)
        return d
        
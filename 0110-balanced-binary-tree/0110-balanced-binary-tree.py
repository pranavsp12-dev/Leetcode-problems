# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if root is None:
                return True
            left=height(root.left)
            right=height(root.right)
            if left is -1:
                return -1
            elif right is -1:
                return -1
        
            elif abs(left-right)>1:
                 return -1
            else:
                 return max(left,right)+1 
        x=height(root)
        if x is -1:
            return False
        else:
            return True

        
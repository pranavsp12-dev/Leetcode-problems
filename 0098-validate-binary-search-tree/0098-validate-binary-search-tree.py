# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(root,low,high):
            if root is None:
                return True
            elif root.val<=low or root.val>=high: # the node value must be in the range
                return False
            else:
                return(check(root.left,low,root.val) and
                check(root.right,root.val,high))
        return check(root, float("-inf"),float("inf")) #intially we keep it has -inf and +inf
            


        
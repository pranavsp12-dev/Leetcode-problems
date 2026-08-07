# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isame(p,q):
            if p is None and q is None:
                return True
            elif p is None or q is None:
                return False
            elif p.val!=q.val:
                return False
            else:
                return isame(p.left,q.left) and isame(p.right,q.right)
       
        if root is None:
                return False
        if isame(root,subRoot):
                return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
            

            
        

        
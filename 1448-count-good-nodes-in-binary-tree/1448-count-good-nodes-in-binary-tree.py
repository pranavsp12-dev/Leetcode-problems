# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count=[0]
        def goodnode(root,count,x):
            if root is None:
                return 
            elif root.val>=x:
                count[0]+=1
            
            goodnode(root.left,count,max(x,root.val))
            goodnode(root.right,count,max(x,root.val))
            return count[0]
        
        
        p=goodnode(root,count,float("-inf"))
        return p
        
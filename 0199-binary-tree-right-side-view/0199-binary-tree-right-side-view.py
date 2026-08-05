# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        arr=[]
        depth=0
        #size=0
        def dfs(root,arr,depth):
            if root is None:
                return
            if depth ==len(arr):
                arr.append(root.val)
                #s#ize=size+1

            dfs(root.right,arr,depth+1)
            dfs(root.left,arr,depth+1)
            return arr
        dfs(root,arr,depth)
        return arr
        
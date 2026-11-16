# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(currP, currQ):
            re1, re2 = 0,0
            
            if not currP and not currQ:
                return True


            if not currP or not currQ or currP.val != currQ.val:
                return False

            return dfs(currP.left, currQ.left) and dfs(currP.right, currQ.right)

        return dfs(p, q)
            



            
        
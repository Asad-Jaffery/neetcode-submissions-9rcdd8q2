# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        LCA = root

        if p.val <= LCA.val and q.val <= LCA.val:
            if p.val == LCA.val:
                return p
            elif q.val == LCA.val:
                return q
            return self.lowestCommonAncestor(LCA.left, p, q)

        elif p.val >= LCA.val and q.val >= LCA.val:
            if p.val == LCA.val:
                return p
            elif q.val == LCA.val:
                return q
            return self.lowestCommonAncestor(LCA.right, p, q)

        else:
            return LCA


        

        # both equal to or greater than node.val
        #   check if equal, 
        # both equal to or less than node.val
        #   check if equal
        # one is greater, and one is less 


        
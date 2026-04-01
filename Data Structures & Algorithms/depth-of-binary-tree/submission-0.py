# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        maxDepth = 1
        stack = [(root, 1)]
        while stack: 
            currPop = stack.pop()
            node = currPop[0]
            depth = currPop[1]
            maxDepth = max(maxDepth, depth)

            if node.right:
                stack.append((node.right, depth + 1))

            if node.left:
                stack.append((node.left, depth + 1))
        
        return maxDepth


        

        
        
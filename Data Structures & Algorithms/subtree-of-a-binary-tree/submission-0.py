# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSame(x, y): 
            if not x and not y:
                return True
            if x and y and (x.val == y.val):
                return isSame(x.left, y.left) and isSame(x.right, y.right)
            else:
                return False
        
        stack = [root]

        while(stack):
            currNode = stack.pop()

            if isSame(currNode, subRoot):
                return True

            if currNode.right:
                stack.append(currNode.right)
            if currNode.left:
                stack.append(currNode.left)
        return False

    
            

       


        
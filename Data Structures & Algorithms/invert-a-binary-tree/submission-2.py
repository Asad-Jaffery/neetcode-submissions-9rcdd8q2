# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        node = root

        if node.left and node.right:
            left = node.left
            node.left = node.right
            node.right = left

            node.right = self.invertTree(node.right)
            node.left = self.invertTree(node.left)
            
        elif node.left:
            node.right = node.left
            node.left = None
            node.right = self.invertTree(node.right)

        elif node.right: 
            node.left = node.right 
            node.right = None
            node.left = self.invertTree(node.left)

        return node
            

        

        
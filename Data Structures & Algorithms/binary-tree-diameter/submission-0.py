# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def depth(node):
            if not node:
                return 0
            
            left_node = depth(node.left)
            right_node = depth(node.right)

            self.ans = max(self.ans , left_node + right_node)

            return 1 + max(left_node , right_node)
        depth(root)
        return self.ans
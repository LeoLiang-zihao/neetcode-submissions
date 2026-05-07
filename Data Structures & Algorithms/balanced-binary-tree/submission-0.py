# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def check(node):
            if not node:
                return True , 0
            left_balanced , left_hight = check(node.left)
            right_balanced , right_hight = check(node.right)

            curbalanced = ( left_balanced
            and right_balanced
            and abs(left_hight - right_hight) <= 1

            )



            return curbalanced , max(left_hight,right_hight) + 1
        balanced ,hight = check(root)
        
        return balanced
# get the height of a tree
"""Given a binary tree, determine if it is height-balanced."""
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def height(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return -1

        l_height = self.height(root.left)
        r_height = self.height(root.right)
        return max(l_height, r_height) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        l_height = self.height(root.left)
        r_height = self.height(root.right)
        if abs(l_height - r_height) <= 1:
            return self.isBalanced(root.left) & self.isBalanced(root.right)
        return False
        

root = TreeNode(
    1,
    TreeNode(2),
    TreeNode(3)
)
root2 = TreeNode(
    3,
    TreeNode(9),
    TreeNode(
        20,
        TreeNode(15),
        TreeNode(7)
    )
)
root3 = TreeNode(
    1,
    TreeNode(
        2,
        TreeNode(
            3,
            TreeNode(4),
            TreeNode(4)
        ),
        TreeNode(3)
    ),
    TreeNode(2)
)
sol = Solution()
print(sol.isBalanced(root))
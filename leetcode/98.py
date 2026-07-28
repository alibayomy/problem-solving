# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        right_nodes = self.addRightNodes(root.right, [])
        left_nodes = self.addLeftNodes(root.left, [])
        if all(val > root.val for val in right_nodes) and all(val < root.val for val in left_nodes):
            return True and self.isValidBST(root.left) and self.isValidBST(root.right)
        return False
    def addRightNodes(self, right_node:Optional[TreeNode], right_nodes_list: list[int]):
        if right_node is None:
            return right_nodes_list
        right_nodes_list.append(right_node.val)
        self.addRightNodes(right_node.left, right_nodes_list)
        self.addRightNodes(right_node.right, right_nodes_list)
        return  right_nodes_list 

    def addLeftNodes(self, node:Optional[TreeNode], left_nodes_list: list[int]):
        if node is None:
            return left_nodes_list
        left_nodes_list.append(node.val)
        self.addLeftNodes(node.left, left_nodes_list)
        self.addLeftNodes(node.right, left_nodes_list)
        return  left_nodes_list 


    def optimizedIsValidBST(self, root: Optional[TreeNode], minVal=float("-inf"), maxVal=float("inf")) -> bool:
        if root is None:
            return True
        print(minVal, root.val, maxVal)
        
        if not (minVal < root.val < maxVal):
            return False
    
        return self.optimizedIsValidBST(root.left, minVal, min(maxVal, root.val)) and self.optimizedIsValidBST(root.right, min(maxVal, root.val), maxVal)
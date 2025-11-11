from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False

        return self.find_leaf(root1) == self.find_leaf(root2)

    def find_leaf(self, node: TreeNode) -> list[int]:
        leaves = []
        if node.left is None and node.right is None:
            return [node.val]
        if node.left:
            leaves.extend(self.find_leaf(node.left))
        if node.right:
            leaves.extend(self.find_leaf(node.right))
        return leaves

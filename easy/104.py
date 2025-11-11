from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_depth = 0
        right_depth = 0

        if root.left is None and root.right is None:
            return 1

        if root.left:
            left_depth = self.maxDepth(root.left)

        if root.right:
            right_depth = self.maxDepth(root.right)

        return max(left_depth, right_depth) + 1

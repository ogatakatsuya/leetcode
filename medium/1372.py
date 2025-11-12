from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.longest = 0
        left = right = 0
        if root.left:
            left = self.longestzigzag(root.left, 0, False, True)
        if root.right:
            right = self.longestzigzag(root.right, 0, True, False)
        return max(left, right)

    def longestzigzag(self, node: TreeNode, current_length: int, from_left: bool, from_right: bool) -> int:
        if node.left is None and node.right is None:
            return current_length + 1

        left = right = 0

        if from_left:
            if node.right:
                # restart
                right = self.longestzigzag(node.right, 0, True, False)
            if node.left:
                # continue
                left = self.longestzigzag(node.left, current_length+1, False, True)
            else:
                # stop and record
                left = current_length+1

        if from_right:
            if node.left:
                # restart
                left =  self.longestzigzag(node.left, 0, False, True)
            if node.right:
                # continue
                right = self.longestzigzag(node.right, current_length+1, True, False)
            else:
                # stop and record
                right = current_length+1

        return max(left, right)
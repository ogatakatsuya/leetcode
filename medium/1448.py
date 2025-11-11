# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.goodnodes(root, -float("inf"))

    def goodnodes(self, node: TreeNode, max_value: int) -> int:
        count = 0
        if node.val >= max_value:
            count += 1
            max_value = node.val
        if node.left:
            count += self.goodnodes(node.left, max_value)
        if node.right:
            count += self.goodnodes(node.right, max_value)
        return count

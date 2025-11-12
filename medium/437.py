from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root is None:
            return 0
        self.target = targetSum
        return self.search(root, [])

    def search(self, node: TreeNode, candidates: list[int]) -> int:
        count = 0

        new_candidates = [x + node.val for x in candidates]
        new_candidates.append(node.val)

        count += sum(1 for x in new_candidates if x == self.target)

        if node.left:
            count += self.search(node.left, new_candidates)
        if node.right:
            count += self.search(node.right, new_candidates)
        return count

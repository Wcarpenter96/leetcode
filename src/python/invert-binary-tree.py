import pdb
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            tmp = root.left
            root.left = root.right
            root.right = tmp
            self.invertTree(root.left)
            self.invertTree(root.right)
            return root


test_left = TreeNode(val=2, left=TreeNode(val=4), right=TreeNode(val=5))
test_right = TreeNode(val=3, left=TreeNode(val=6), right=TreeNode(val=7))
test_root = TreeNode(val=1, left=test_left, right=test_right)
test1 = Solution().invertTree(test_root)  # call inorder function with visited stack
print(test1)

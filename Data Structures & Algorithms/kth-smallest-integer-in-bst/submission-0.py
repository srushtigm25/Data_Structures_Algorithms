# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = []

        def inorder(node):
            # Base case
            if not node:
                return 

            # Traverse left
            inorder(node.left)

            # Store current node
            result.append(node.val)

            # Traverse right
            inorder(node.right)

        inorder(root)

        return result[k - 1]
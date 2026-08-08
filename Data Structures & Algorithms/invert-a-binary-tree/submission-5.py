# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        def dfs(node):
            if node is None:
                return
            temp = node.left
            node.left = node.right
            node.right = temp

            dfs(node.right)
            dfs(node.left)

            return node

        return dfs(root)
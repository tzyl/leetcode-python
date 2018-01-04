# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        inorder= []
        self.inorder_traversal_helper(root, inorder)
        return inorder

    def inorder_traversal_helper(self, root, inorder):
        if root is not None:
            self.inorder_traversal_helper(root.left, inorder)
            inorder.append(root.val)
            self.inorder_traversal_helper(root.right, inorder)


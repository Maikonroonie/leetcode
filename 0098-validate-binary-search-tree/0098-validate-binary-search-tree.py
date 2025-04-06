# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        def rek(root, l=float('-inf'), r=float('inf')):
            if not root:
                 return True
            if root.val<=l or root.val>=r:
                return False
            return rek(root.left, l, root.val) and rek(root.right, root.val, r)
        return rek(root)
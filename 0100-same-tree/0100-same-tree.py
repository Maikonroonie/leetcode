# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        def rek(p,q):
            if not p and not q: return True
            if not p and q or not q and p: return False
            if p.val!=q.val: return False
            return rek(p.left, q.left) and rek(p.right, q.right)
        return(rek(p,q))
        



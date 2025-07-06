# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        result=[]

        def rek(v, target, path):
            if not v:
                return
            
            path.append(v.val)
            target-=v.val

            if v.left is None and v.right is None and target == 0:
                result.append(list(path))
            else:
                rek(v.left, target, path)
                rek(v.right, target, path)
            path.pop()
        
        rek(root, targetSum, [])
        return result

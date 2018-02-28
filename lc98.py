# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isvalid(root,float("-inf"),float("inf"))
        
        
    def isvalid(self, root, minv, maxv):
        if root == None:
            return True
        if not (minv < root.val < maxv):
            return False
        return self.isvalid(root.left,minv,root.val) and self.isvalid(root.right,root.val,maxv)
    
        
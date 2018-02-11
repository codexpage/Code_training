# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root ==None:
            return None
        values = self.dfs(root)
        min_v = float("inf")
        for i in range(len(values)-1):
            diff = abs(values[i+1]-values[i])
            min_v = min(diff,min_v)
            
        return min_v
    def dfs(self, node):
        values=[]
        if node.left!=None:
            values.extend(self.dfs(node.left))
            
        values.append(node.val)

        if node.right!=None:
            values.extend(self.dfs(node.right))
    
        return values
            
        
#assume the None node has two None children will make the problem easy
#when both node is None, return 


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        return self.dfs(t1,t2)
    
    def dfs(self,t1,t2):
        if t1==None and t2==None:
            return None
        node = TreeNode(0)
        #at least one of it is not null
        t1_left=None
        t1_right=None
        t2_left=None
        t2_right=None
        if t1!=None:
            # print("t1:",t1.val)
            t1_left=t1.left
            t1_right=t1.right
            node.val+=t1.val
        if t2!=None:
            # print("t2:",t2.val)
            t2_left=t2.left
            t2_right=t2.right
            node.val+=t2.val

        # print("left",t1_left,t2_left)
        node.left = self.dfs(t1_left,t2_left)
        # print("right",t1_right,t2_right)
        node.right = self.dfs(t1_right,t2_right)
        # print("back")
        print(node.val)
        return node
        
            
        
            
        
        
        
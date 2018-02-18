# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



#speed too slow !


# class Solution:
#     def isSymmetric(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
#         que=[root]
#         while True:
#             level=[]
#             for q in que:
#                 level.append(q.left if q!=None else None)
#                 level.append(q.right if q!=None else None)
#             if level==[None]*len(level):
#                 return True
#             if not self.isPalindromic(level):
#                 return False
#             que=list(level)
            
#     def isPalindromic(self,l):
#         # print(l,type(l))
#         lforward = [(x.val if x else None) for x in l]
#         lbackward = list(lforward)
#         lbackward.reverse()
#         # print(lforward,lbackward,lforward==lbackward)
#         if lforward==lbackward:
#             return True
#         else:
#             return False
        
#very fast solution using recursion  

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        return self.isMirror(root.left,root.right)
    def isMirror(self,r1,r2):
        if r1==None and r2==None:
            return True
        if r1==None or r2==None:
            return False
        return r1.val==r2.val and self.isMirror(r1.right,r2.left) and self.isMirror(r1.left,r2.right)
        
        
            
            
                
                
        
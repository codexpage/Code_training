# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#count from back, it's easy to think about recursive method.
#when backtrack, we count the backward order. 
#if we want to delete a node in single list, we need to get it's prior node
#so in recursion, we need to find n+1 th node. 
#boundary case:  delete last element : as usual 
#delete first element- use a dummy node easily solve the problem
class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        length = self.getlist(dummy,n)
        return dummy.next
        
    def getlist(self,head,n):
        if head.next==None:
            return 1
        else:
            order = self.getlist(head.next,n)+1
            if order == n+1:
                head.next = head.next.next
            return order
              
            
        
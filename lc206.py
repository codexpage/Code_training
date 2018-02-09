# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

#in the recursion return back, it's a backwards traverse, so will can make use of this point
#the point is cancel and switch pointers backwards is much easier than forward
class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        if head.next == None:
            return head
        return self.reverse_next(head)
        
    def reverse_next(self, cur):
        if cur.next.next == None:
            cur.next.next = cur
#             print(cur.val,"<-",cur.next.val)
            ret = cur.next
            cur.next = None
            return ret
        else:
            new_head = self.reverse_next(cur.next)
            cur.next.next = cur
#             print(cur.val,"<-",cur.next.val)
            cur.next = None
            return new_head
        
            
        
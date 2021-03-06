# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None or head.next == None or head.next.next == None:
            return False
        fast = head.next.next
        slow = head.next
        while True:
            if fast == slow:
                return True
            if fast.next==None or fast.next.next==None:
                return False
            fast = fast.next.next
            slow = slow.next
#fast and slow pointer: http://www.cnblogs.com/hxsyl/p/4395794.html
# for how to detect the cycle start
# you need to know some background knowledge, it's very clever idea
# for the fast-slow-meet-point and head point, step 1,finally they must meet at the cycle start 

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None or head.next.next == None:
            return None
        fast = head.next.next
        slow = head.next
        while True:
            if fast == slow:
                break
            if fast.next==None or fast.next.next==None:
                return None
            fast = fast.next.next
            slow = slow.next
        h = head
        while True:
            if slow == h:
                return h
            slow = slow.next
            h = h.next
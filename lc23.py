#the merge2 is copied for problem merge 2 list
#we only need to make a divide and conquer 
#is not hard if you have implement merge2 function

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists)==0:
            return []
        if len(lists)==1:
            return lists[0]
        if len(lists)==2:
            return self.merge2(lists[0],lists[1])
        mid = len(lists)//2
        sublists = [self.mergeKLists(lists[:mid]),self.mergeKLists(lists[mid:])]
        return self.mergeKLists(sublists)
    def merge2(self,l1,l2):
        res=ListNode(0)
        pos=res
        if not l1:
            return l2
        if not l2:
            return l1
        while True:
            if l1.val<l2.val:
                pos.next=l1
                pos=pos.next
                if not l1.next:
                    pos.next=l2
                    return res.next
                else:
                    l1=l1.next
            else:
                pos.next=l2
                pos=pos.next
                if not l2.next:
                    pos.next=l1
                    return res.next
                else:
                    l2=l2.next

            
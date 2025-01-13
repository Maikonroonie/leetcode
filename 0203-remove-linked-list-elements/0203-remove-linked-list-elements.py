# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        while head and head.val==val:
            head=head.next
        if not head or not head.next:
            return head
        cur=head
        prev=cur
        cur=cur.next
        while cur:
            if cur.val==val:
                prev.next=cur.next
            else:
                prev=cur
            cur=cur.next
        return head

        
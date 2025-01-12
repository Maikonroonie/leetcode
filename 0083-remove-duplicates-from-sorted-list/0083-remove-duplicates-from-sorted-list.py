# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head
        while head.next and head.val==head.next.val:
            head=head.next
        prev=head
        cur=head.next
        while cur:
            if prev.val==cur.val:
                prev.next=cur.next
            else:
                prev=cur
            cur=cur.next
        return head
        
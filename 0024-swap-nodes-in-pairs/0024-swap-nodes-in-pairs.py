# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        if not head or not head.next:
            return head
        new_head=head.next
        prev=None
        cur=head
        #reverse parami
        while cur and cur.next:
            next_p=cur.next.next
            sec=cur.next
            sec.next=cur
            cur.next=next_p
            if prev:
                prev.next=sec

            prev=cur
            cur=next_p
        return new_head



        
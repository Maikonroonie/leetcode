# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if not head or not head.next or k==0:
            return head
        cur=head
        len=1
        while cur.next:
            cur=cur.next
            len+=1
        k=k%len
        if k==0:
            return head
        new_tail_idx=len-k-1
        new_tail=head
        for _ in range(new_tail_idx):
            new_tail=new_tail.next
        new_head=new_tail.next
        new_tail.next=None
        cur.next=head
        return new_head

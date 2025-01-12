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
        prev=ListNode(0, head)
        cur=head
        cnt=0
        start=head
        while cnt !=k:
            start=cur
            prev=ListNode(0,cur)
            while cur.next:
                prev=cur
                cur=cur.next
            prev.next=None
            cur.next=start
            cnt+=1
        return cur
                

            
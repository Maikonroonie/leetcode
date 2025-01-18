# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry=0
        Dummy= ListNode(0)
        Dummy_cp=Dummy
        while l1 or l2 or carry:
            l11=l1.val if l1 else 0
            l22=l2.val if l2 else 0
            val=l11+l22+carry
            carry=val//10
            val=val%10
            Dummy.next=ListNode(val)
            Dummy=Dummy.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        return Dummy_cp.next
        
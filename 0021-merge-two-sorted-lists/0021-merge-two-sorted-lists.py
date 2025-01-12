# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        m=ListNode(0)
        m_cp=m
        cur1=list1
        cur2=list2
        while cur1 and cur2:
            if cur1.val>cur2.val:
                m.next=cur2
                cur2=cur2.next
            else:
                m.next=cur1
                cur1=cur1.next
            m=m.next
        if cur1:
            m.next=cur1
        elif cur2:
            m.next=cur2
        return m_cp.next
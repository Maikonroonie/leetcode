class Solution(object):
    def partition(self, head, x):
        if not head or not head.next:
            return head
        smaller_head = ListNode(0)
        greater_head = ListNode(0)
        
        smaller = smaller_head
        greater = greater_head
        cur = head        
        while cur:
            if cur.val < x:
                smaller.next = cur
                smaller = smaller.next
            else:
                greater.next = cur
                greater = greater.next
            cur = cur.next
        
        greater.next = None
        
        smaller.next = greater_head.next
        
        return smaller_head.next

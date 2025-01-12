class Solution(object):
    def partition(self, head, x):
        if not head or not head.next:
            return head
        
        # Dummy nodes for "smaller" and "greater/equal" lists
        smaller_head = ListNode(0)
        greater_head = ListNode(0)
        
        # Pointers to iterate and build the two lists
        smaller = smaller_head
        greater = greater_head
        cur = head
        
        while cur:
            if cur.val < x:
                # Add to the "smaller" list
                smaller.next = cur
                smaller = smaller.next
            else:
                # Add to the "greater/equal" list
                greater.next = cur
                greater = greater.next
            cur = cur.next
        
        # Terminate the "greater" list to avoid cycles
        greater.next = None
        
        # Connect "smaller" list to the "greater/equal" list
        smaller.next = greater_head.next
        
        # Return the head of the "smaller" list
        return smaller_head.next

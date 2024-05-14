#single
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            cur = curr.next
            curr.next = prev
            prev = curr
            curr = cur
        return prev 
#doubled 
def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            cur = curr.next
            curr.next = prev
            curr.prev = cur
            prev = curr
            curr = cur
        return prev 

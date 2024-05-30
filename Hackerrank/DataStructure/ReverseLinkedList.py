def reverse(llist):
    # Write your code here
    prev, cur = None, llist
    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
    return prev

# without using any built-in hash table libraries
# using an array with linked list
class ListNode:
    def __init__(self,key = -1,val = -1,next=None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:
    def __init__(self):
        self.hashmap =[ListNode(0) for i in range(1000)]
    
    def hash(self,key):
        return key % len(self.hashmap)

    def put(self, key: int, value: int) -> None:
        cur = self.hashmap[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = ListNode(key,value)

    def get(self, key: int) -> int:
        cur = self.hashmap[self.hash(key)]
        while cur.next:
            if cur.next.key == key:
                return cur.next.val
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        cur = self.hashmap[self.hash(key)]
        while cur and cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next
        

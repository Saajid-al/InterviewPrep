class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next




class Solution:
    def reverseList(self, head):
        prev = None

        curr = head
        while(curr):
            
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev
    def printLinkedList(self,head):
        curr = head
        while(curr):
            print(curr.val, end="->" if curr.next else "\n" )
            curr = curr.next


s = Solution()
a = ListNode(5)
b = ListNode(10)
c = ListNode(15)
a.next = b
b.next = c

s.printLinkedList(a)
s.printLinkedList(s.reverseList(a))

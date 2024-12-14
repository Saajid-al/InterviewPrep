# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNodes(self, head):
        curr = head
        while(curr.next)
            while(curr.val > curr.next.val):
                
    
    def printLinkedList(self, head):
        curr = head

        while(curr):
            print(curr.val, end="->" if curr.next else "\n" )
            curr = curr.next
        
def main():
    s = Solution()

    a = ListNode(5)
    b = ListNode(2)
    c = ListNode(13)
    d = ListNode(3)
    e = ListNode(8)

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    s.printLinkedList(a)

    print(s.removeNodes(a))

if __name__ == "__main__":
    main()
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(0)
        dummyNode.next = head
        curr = head
        stack = []
        prev = None
        while(curr):
            stack.append(curr.val)
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        maxElement = prev.val
        previousDummy = ListNode(0)
        previousDummy.next = prev
        dummy = ListNode(0)
        dummy.next = prev

        while(prev): #we found a max Element
            if prev.val>=maxElement:
                maxElement = prev.val
                previousDummy = prev
                prev = prev.next
            else:
                previousDummy.next = prev.next
                prev = prev.next
                

        #reverse the list once again to return properly
        curr2 = dummy.next
        previous = None
        while(curr2):
            nxt = curr2.next
            curr2.next = previous
            previous = curr2
            curr2 = nxt


        return previous


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
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        slow = head
        fast = head

        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None
        prev = None

        while(second):
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        curr = head
        
        while(prev):
            temp1 = curr.next
            temp2 = prev.next

            curr.next = prev
            prev.next = temp1

            curr = temp1
            prev = temp2






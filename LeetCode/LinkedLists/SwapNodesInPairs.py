# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        #[1,2,3]
        #[2,1,3]
        dummy = ListNode(0, head) 
        curr = head
        prev = dummy
        while(curr and curr.next): 
            nxtEle = curr.next.next #set the next element to be the element after the switched element
            nxt = curr.next #keeping our next element in a var

            nxt.next = curr #the 2nd element now points to our first one
            curr.next = nxtEle #our current element.next now points to our element past the 2nd one
            prev.next = nxt  #reversing 

            prev = curr #our previous element is now our current
            curr = nxtEle #continue down the cycle

        return dummy.next
            

s = Solution()
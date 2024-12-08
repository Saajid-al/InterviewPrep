class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def pairSum(self, head) :

        slow = head
        fast = head
        prev = None
        while(fast and fast.next): #slow and fast pointer
            fast = fast.next.next
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt #we start reverseing the array
            #once the array is at the mid way point we can compare the 2 values. We're basically just starting from the midle and comparing 
            #inwwads instead of outwards
        
        maxTwin = 0
        while prev:
            maxTwin = max(maxTwin, prev.val + slow.val)
            prev = prev.next
            slow = slow.next
        
        return maxTwin
        

s = Solution()

a = ListNode(5)
b = ListNode(4)
c = ListNode(2)
d = ListNode(1)
a.next = b
b.next = c
c.next = d
print(s.pairSum(a))

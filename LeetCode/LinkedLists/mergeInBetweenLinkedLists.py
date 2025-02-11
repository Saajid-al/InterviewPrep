class Node():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeInBetween(self, list1,a, b, list2):
        
        
        curr = list1
        i = 0
        while i < a-1:
            curr = curr.next
            i+=1
        head = curr
        while(i<=b):
            curr = curr.next
            i+=1
        head.next = list2
        while(list2.next):
            list2 = list2.next
        list2.next = curr

        return list1

def main():
    a = Node(1)
    b = Node(2)
    c = Node(3)
    a.next = b
    b.next = c


if __name__ == "__main__":
    main()

        
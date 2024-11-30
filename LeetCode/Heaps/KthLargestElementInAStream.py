import heapq


class KthLargest:

    def __init__(self, k, nums):
        self.minHeap = nums
        self.k = k

        heapq.heapify(self.minHeap)
        while(len(self.minHeap) > k): # keeping only the top 3 elements.
            heapq.heappop(self.minHeap) # pushes out the smallest elements
        

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:  #RETURNS THE 3RD LARGEST (KTH LARGEST)
            heapq.heappop(self.minHeap)
        return self.minHeap[0]


def main():
    # Test Case 1: Initialize KthLargest with k=3 and nums=[4, 5, 8, 2]
    k = 3
    nums = [4, 5, 8, 2]

    kthLargest = KthLargest(k, nums)
    print("Initial KthLargest object created with nums:", nums)
    print("Expected k-th largest after initialization:", kthLargest.minHeap[0])  # Expected: 4

    # Test Case 2: Add elements and check the k-th largest
    print("Add 3, Expected k-th largest: 4, Got:", kthLargest.add(3))  
    print("Add 5, Expected k-th largest: 5, Got:", kthLargest.add(5))  
    print("Add 10, Expected k-th largest: 5, Got:", kthLargest.add(10))  
    print("Add 9, Expected k-th largest: 8, Got:", kthLargest.add(9)) 
    print("Add 4, Expected k-th largest: 8, Got:", kthLargest.add(4))  

if __name__ == "__main__":
    main()



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

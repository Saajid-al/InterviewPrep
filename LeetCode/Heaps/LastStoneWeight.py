import heapq


class Solution:
    def lastStoneWeight(self, stones):
        
        heapq.heapify(stones)
        while(len(stones) > 1):
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            if x != y: 
                heapq.heappush(stones, y-x)

        if not stones:
            stones.append(0)
        return stones[0]
            
        




def main():

    s = Solution()
    print(s.lastStoneWeight([2,7,4,1,8,1]))

if __name__ == "__main__":
    main()
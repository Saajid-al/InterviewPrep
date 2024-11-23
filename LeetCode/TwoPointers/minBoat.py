class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:


            
        l = 0
        r = len(people)-1
        minBoat = 0
        people.sort()

        while(l<=r):
            if people[l]+people[r] <= limit:
                l+=1
            r-=1
            minBoat +=1
        return minBoat


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:


            
        l = 0
        r = len(people)-1
        minBoat = 0
        people.sort()

        while(l<=r):
            if people[l]+people[r] <= limit:
                l+=1
            r-=1
            minBoat +=1
        return minBoat


s = Solution()
print(s.numRescueBoats([3,2,2,1], 3))
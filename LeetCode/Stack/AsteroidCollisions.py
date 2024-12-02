class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        
        for i in range(len(asteroids)):
            if not stack:
                stack.append(asteroids[i]) # 5 10 
            
            if stack[-1] < 0 and asteroids[i] < 0 or stack[-1] > 0 and asteroids[i] > 0:
                stack.append(asteroids[i])
            elif abs(stack[-1] == abs(asteroids[i])):
                stack.pop()
            elif abs(stack[-1]) > abs(asteroids[i]):
                continue
            elif abs(stack[-1]) < abs(asteroids[i]):
                stack.pop()
                stack.append(asteroids[i])

        return stack


s = Solution()
print(s.asteroidCollision([5,10,-5]))
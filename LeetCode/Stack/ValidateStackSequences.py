class Solution:
    def validateStackSequences(self, pushed, popped):
        stack =  []
        for i in pushed:
            stack.append(i)
            while i < len(popped) and stack and popped[i] == stack[-1]:
                stack.pop()
                i+=1

        return not stack

def main():
    s = Solution()
    print(s.validateStackSequences([1,2,3,4,5], [4,5,3,2,1]))



if __name__ == "__main__":
    main()
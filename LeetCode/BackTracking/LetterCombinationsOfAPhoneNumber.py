from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
         
        hashmap = {1:[2,3,4]}
        print(hashmap[1])


def main():
    s = Solution()
    s.letterCombinations("23")



if __name__ == "__main__":
    main()
import collections

class Solution:
    def firstUniqChar1(self, s: str) -> int:
        for letter in s:
            if s.count(letter) == 1:
                return s.index(letter)
        return -1

    def firstUniqChar2(self, s):
        hash_set = collections.Counter(s)
        # Traverse the string from the beginning...
        for idx in range(len(s)):
            # If the count is equal to 1, it is the first distinct character in the list.
            if hash_set[s[idx]] == 1:
                return idx
        return -1  # If no character appeared exactly once...


test1 = Solution().firstUniqChar1("leetcode")
print(test1)

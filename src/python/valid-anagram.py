from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return "".join(sorted(s)) == "".join(sorted(t))

    def isAnagram2(self, s: str, t: str) ->  bool:
        count = defaultdict(int)

        # Count the frequency of characters in string s
        for x in s:
            count[x] += 1

        # Decrement the frequency of characters in string t
        for x in t:
            count[x] -= 1

        # Check if any character has non-zero frequency
        for val in count.values():
            if val != 0:
                return False

        return True


test = Solution().isAnagram2(s = "anagram", t = "nagaram")
print(test)
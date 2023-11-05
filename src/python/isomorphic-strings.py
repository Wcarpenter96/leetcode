class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Create a character map
        char_map = {}
        for i, char in enumerate(s):
            if char in char_map:
                # Mapping should not be many-to-one
                if char_map[char] != t[i]:
                    return False
            else:
                char_map[char] = t[i]
        print(char_map)
        # Check if the map is NOT one-to-many and onto
        return len(char_map) == len(set(char_map.values())) and all([char in char_map.values() for char in t])

    def isIsomorphic2(self, s: str, t: str) -> bool:
        d = {}
        seen = set()
        for i, j in zip(s, t):
            if i in d:
                if d[i] != j:
                    return False
            else:
                if j in seen:
                    return False
                seen.add(j)
                d[i] = j
        return True


test1 = Solution().isIsomorphic(s="egg", t="add")
print(test1)
test2 = Solution().isIsomorphic(s="paper", t="title")
print(test2)
test3 = Solution().isIsomorphic(s="foo", t="bar")
print(test3)
test4 = Solution().isIsomorphic(s="bbbaaaba", t="aaabbbba")
print(test4)
test5 = Solution().isIsomorphic(s="badc", t="baba")
print(test5)
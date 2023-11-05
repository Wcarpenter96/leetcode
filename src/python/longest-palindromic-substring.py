class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Time complexity : O(n^3). Assume that n is the length of the input string,
        there are a total of C(n, 2) = n(n-1)/2 substrings
        (excluding the trivial solution where a character itself is a palindrome).
        Since verifying each substring takes O(n) time, the run time complexity is O(n^3).

        Space complexity : O(1).
        """
        longest_palindrome = ""
        for i in range(len(s)):
            for j in range(1, len(s)+1):
                subs = s[i:j]
                if len(subs) > len(longest_palindrome) and subs == subs[::-1]:
                    longest_palindrome = s[i:j]
        return longest_palindrome

    def longestPalindrome2(self, s: str) -> str:
        """
        Time complexity : O(n^2).
        Since expanding a palindrome around its center could take O(n) time, the overall complexity is O(n^2).

        Space complexity : O(1).
        """
        if len(s) <= 1:
            return s

        def expand_from_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        max_str = s[0]

        for i in range(len(s) - 1):
            odd = expand_from_center(i, i)
            even = expand_from_center(i, i + 1)

            if len(odd) > len(max_str):
                max_str = odd
            if len(even) > len(max_str):
                max_str = even

        return max_str


test1 = Solution().longestPalindrome("a")
print(test1)


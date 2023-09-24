from itertools import zip_longest


class Solution:
    def wordPattern1(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        letter_to_word = {}
        word_to_letter = {}
        # base case
        if len(words) != len(pattern):
            return False
        for i, letter in enumerate(pattern):
            word = words[i]
            existing_word = letter_to_word.get(letter)
            existing_letter = word_to_letter.get(word)
            # check if map is one-to-one
            if (existing_word and existing_word != word) or (existing_letter and existing_letter != letter):
                return False
            else:
                letter_to_word[letter] = word
                word_to_letter[word] = letter
        # check if map is onto
        if set(letter_to_word.keys()) == set(list(pattern)):
            return True
        return False

    def wordPattern2(self, pattern: str, s: str) -> bool:

        s = s.split()

        return (len(set(pattern)) ==
                len(set(s)) ==
                len(set(zip_longest(pattern, s))))


test1 = Solution().wordPattern2(pattern="abba", s="dog cat cat dog")
print(test1)

test2 = Solution().wordPattern2(pattern="aaaa", s="dog cat cat dog")
print(test2)

test3 = Solution().wordPattern2(pattern="abba", s="dog dog dog dog")
print(test3)

test4 = Solution().wordPattern2(pattern="aaa", s="aa aa aa aa")
print(test4)
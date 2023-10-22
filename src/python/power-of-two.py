class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        m = 1
        while m <= n:
            if m == n:
                return True
            m = m * 2
        return False

    def isPowerOfTwoV2(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True
        while n % 2 == 0:
            n = n/2
        return n == 1

    def isPowerOfTwoV3(self, n: int) -> bool:
        # This is crazy
        return bin(n)[2] == "1" and bin(n).count("1") == 1


test1 = Solution().isPowerOfTwo(16)
print(test1)

test2 = Solution().isPowerOfTwo(112343455)
print(test2)

test3 = Solution().isPowerOfTwo(-16)
print(test3)

test4 = Solution().isPowerOfTwoV2(16)
print(test4)

test5 = Solution().isPowerOfTwoV3(16)
print(test5)

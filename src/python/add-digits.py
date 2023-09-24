class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            num = sum(int(i) for i in str(num))
        return num


test1 = Solution().addDigits(38)
print(test1)
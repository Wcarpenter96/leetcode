# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    if version > 3:
        return True
    return False


class Solution:
    def firstBadVersion(self, n: int) -> int:
        def binary_search(low, high):
            # This means the lower version is good and the higher version is bad. Return the high version
            print(low, high)
            if low + 1 == high:
                return high
            mid = (low + high) // 2
            # If the middle version is bad, search for a lower bad version
            if isBadVersion(mid):
                return binary_search(low, mid)
            # If the middle version is good, search for a higher bad version
            else:
                return binary_search(mid, high)

        return binary_search(0, n)


test = Solution().firstBadVersion(n=100)
print(test)

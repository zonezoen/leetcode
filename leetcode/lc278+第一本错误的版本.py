class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1 and self.isBadVersion(n):
            return 1

        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            mid_bool = self.isBadVersion(mid)
            if mid_bool and not self.isBadVersion(mid-1):
                return mid
            if mid_bool:
                right = mid - 1
            else:
                left = mid + 1

    def isBadVersion(self,version):
        return True

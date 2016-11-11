# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end = 1, n
        mid = (start + end) / 2
        ans = guess(mid)
        while ans != 0 and start != end:
            if ans == 1:
                start = mid + 1
            else:
                end = mid - 1
            mid = (start + end) / 2
            ans = guess(mid)
        return mid

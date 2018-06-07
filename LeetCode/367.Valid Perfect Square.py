class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1: return True
        start, end = 1, num
        while start != end and start < end:
            mid = (start + end) / 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                start = mid + 1
            else:
                end = mid
        return False

    def isPerfectSquare2(self, num):
        if num == 1: return True
        record = set()
        inx = 2
        while inx <= num:
            i = inx
            if i * i > num:
                return False
            if i not in record:
                while i * i <= num:
                    i *= i
                    if i == num:
                        return True
                    record.add(i)
            inx += 1
        return False

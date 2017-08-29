class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        n = 1
        while n <= num:
            n = n << 1
        return (n - 1) ^ num

    def findComplement2(self, num):
        if num == 0:
            return 1

        rst, n = 0, 1
        while num > 0:
            if num & 1 == 0:
                rst |= n
            num = num >> 1
            n = n << 1
        return rst

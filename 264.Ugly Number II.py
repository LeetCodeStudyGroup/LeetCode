class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [2, 3, 5]
        cnts = [0, 0, 0]
        result = [1]
        for i in range(n - 1):
            vals = [nums[x] * result[cnts[x]] for x in range(3)]
            inx = 0
            if vals[inx] > vals[1]:
                inx = 1
            if vals[inx] > vals[2]:
                inx = 2
            for j in range(3):
                if vals[j] == vals[inx]:
                    cnts[j] += 1
            result.append(vals[inx])
        return result[-1]

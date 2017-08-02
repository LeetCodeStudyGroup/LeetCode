class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        count = 0
        map1 = self.two_sum(A, B)
        map2 = self.two_sum(C, D)
        for key in map1.keys():
            if -key in map2:
                count += map1[key] * map2[-key]
        return count

    def two_sum(self, A, B):
        rst = {}
        for num1 in A:
            for num2 in B:
                val = num1 + num2
                if val in rst:
                    rst[val] += 1
                else:
                    rst[val] = 1
        return rst

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        self.add(result, [], n, k, 1)
        return result
        
    def add(self, result, array, n, k, inx):
        if k == len(array):
            result.append(array)
            return
        elif inx > n or n + 1 - inx < k - len(array):
            return

        self.add(result, array[:], n , k, inx + 1)
        array.append(inx)
        self.add(result, array, n , k, inx + 1)

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """

        start = 0
        end = n
        
        while start + 1 < end:
            mid = int(start + (end - start) / 2)
            
            if isBadVersion(mid):
                end = mid
            else:
                start = mid
        
        if isBadVersion(start):
            return start
        
        if isBadVersion(end):
            return end
        
        return 0

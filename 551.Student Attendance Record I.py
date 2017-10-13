class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return s.count('A') < 2 and 'LLL' not in s
    
    def checkRecord2(self, s):
        absent = late = 0
        for i, c in enumerate(s):
            if c == 'A':
                absent += 1
                late = 0
            elif c == 'L':
                late += 1
            else:
                late = 0
            if late == 3 or absent == 2:
                return False
        return True

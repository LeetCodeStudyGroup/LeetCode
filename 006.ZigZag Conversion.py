class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        zigzag = []
        for i in range(numRows):
            zigzag.append([])

        i = col = 0
        while i < len(s):
            if col % 2 == 1 and numRows != 2:
                inx = numRows - 2
                while inx > 0 and i < len(s):
                    zigzag[inx].append(s[i])
                    i += 1
                    inx -= 1
            else:
                for row in range(numRows):
                    if i < len(s):
                        zigzag[row].append(s[i])
                        i += 1
            col += 1
        result = ""
        for row in zigzag:
            for item in row:
                result += item
        return result

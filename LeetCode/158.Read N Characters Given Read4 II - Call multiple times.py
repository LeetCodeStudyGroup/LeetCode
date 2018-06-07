# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def __init__(self):
        self.buf = [''] * 4
        self.size = read4(self.buf)
        self.inx = 0

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        inx = 0
        while n > 0 and self.size > 0 and inx < n:
            buf[inx] = self.buf[self.inx]
            self.inx += 1
            inx += 1
            if self.inx == self.size:
                self.size = read4(self.buf)
                self.inx = 0
        return inx

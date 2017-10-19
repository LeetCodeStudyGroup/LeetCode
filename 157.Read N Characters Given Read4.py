# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        inx, cnt = 0, 0
        tmp = [''] * 4
        while inx < n:
            cnt = read4(tmp)
            if cnt == 0:
                break
            for i in range(cnt):
                if inx == n:
                    break
                buf[inx] = tmp[i]
                inx += 1
        return inx

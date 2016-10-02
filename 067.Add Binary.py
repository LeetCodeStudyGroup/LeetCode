class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = []
        i = len(a) - 1
        j = len(b) - 1
        carry = '0'
        while i >= 0 and j >= 0:
            carry = self.convert(result, a[i], b[j], carry)
            i -= 1
            j -= 1
        r, inx = (a, i) if i >= 0 else (b, j)
        while inx >= 0:
            carry = self.convert(result, r[inx], carry)
            inx -= 1
        if carry == '1':
            result.append('1')
        return ''.join(result[::-1])

    def convert(self, result, a, b, c='0'):
        x = int(a) + int(b) + int(c)
        carry = '0'
        if x == 3:
            result.append('1')
            carry = '1'
        elif x == 2:
            result.append('0')
            carry = '1'
        elif x == 1:
            result.append('1')
        else:
            result.append('0')
        return carry

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = []
        i = len(num1) - 1
        j = len(num2) - 1
        c = '0'
        while i >= 0 and j >= 0:
            r, c = self.add_char(num1[i], num2[j], c)
            result.append(r)
            i -= 1
            j -= 1
        while i >= 0:
            r, c = self.add_char(num1[i], c, '0')
            result.append(r)
            i -= 1
        while j >= 0:
            r, c = self.add_char(num2[j], c, '0')
            result.append(r)
            j -= 1
        if c != '0':
            result.append(c)
        return ''.join(result[::-1])
        
    def add_char(self, c1, c2, c3):
        c = '0'
        result = ord(c1) + ord(c2) + ord(c3) - ord('0') - ord('0')
        if result > ord('9'):
            c = '1'
            result = ord(c1) + ord(c2) + ord(c3) - ord('9') - ord('1')
        return chr(result), c

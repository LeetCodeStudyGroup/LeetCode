class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        str1, rst = [int(num1[i]) for i in range(len(num1) - 1, -1, -1)], []
        for i in range(len(num2)):
            self.add(rst, self.mul(str1, int(num2[len(num2) - i - 1])), i)
        while len(rst) > 1 and rst[-1] == 0:
            rst.pop()
        return ''.join(str(s) for s in reversed(rst))

    def add(self, a, b, offset):
        size, c = min(len(a), len(b) + offset), 0
        for i in range(offset, size):
            a[i] += b[i - offset] + c
            c = a[i] / 10
            a[i] %= 10
        if len(a) < len(b) + offset:
            for i in range(size, len(b) + offset):
                r = b[i - offset] + c
                c = r / 10
                a.append(r % 10)
        elif len(a) > len(b) + offset:
            for i in range(size, len(a)):
                a[i] += c
                c = a[i] / 10
                a[i] %= 10
        if c > 0:
            a.append(c)

    def mul(self, s, num):
        rst, c = [], 0
        for n in s:
            r = n * num + c
            c = r / 10
            rst.append(r % 10)
        if c > 0:
            rst.append(c)
        return rst

    def multiply_str_version(self, num1, num2):
        str1, str2, rst = list(num1), list(num2), []
        str1.reverse()
        str2.reverse()
        for i in range(len(str2)):
            self.str_add(rst, self.str_mul(str1, str2[i]), i)
        while len(rst) > 1 and rst[-1] == '0':
            rst.pop()
        return ''.join(reversed(rst))

    def str_add(self, a, b, offset):
        size, c = min(len(a), len(b) + offset), '0'
        for i in range(offset, size):
            a[i], c = self.chr_add(a[i], b[i - offset], c)
        if len(a) < len(b) + offset:
            for i in range(size, len(b) + offset):
                r, c = self.chr_add(b[i - offset], c, '0')
                a.append(r)
        elif len(a) > len(b) + offset:
            for i in range(size, len(a)):
                a[i], c = self.chr_add(a[i], c, '0')
        if c != '0':
            a.append(c)

    def str_mul(self, s, num):
        rst, c = [], '0'
        for char in s:
            r, new_c = self.chr_mul(char, num)
            r, c = self.chr_add(r, c, '0')
            c = self.chr_add(c, new_c, '0')[0]
            rst.append(r)
        if c != '0':
            rst.append(c)
        return rst

    def chr_add(self, a, b, c):
        rst = int(a) + int(b) + int(c)
        return str(rst % 10), str(rst / 10)

    def chr_mul(self, a, b):
        rst = int(a) * int(b)
        return str(rst % 10), str(rst / 10)

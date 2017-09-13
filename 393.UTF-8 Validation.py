class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        if len(data) == 0:
            return False
        count = 0
        for d in data:
            if count == 0:
                if d >> 7 == 0:
                    continue
                elif d >> 3 == int('11110', 2):
                    count = 3
                elif d >> 4 == int('1110', 2):
                    count = 2
                elif d >> 5 == int('110', 2):
                    count = 1
                else:
                    return False
            else:
                if d >> 6 != int('10', 2):
                    return False
                count -= 1
        return count == 0

    def validUtf8_2(self, data):
        if len(data) == 0:
            return False
        self.index = 0
        while self.index < len(data):
            if not self.valid():
                return False
        return True

    def valid(self, data):
        count = self.bit_count(data[self.index])
        self.index += 1
        if count == 0:
            return True
        if count == 1:
            return False

        for i in range(count - 1):
            if data[self.index] & (1 << 7) == 0 or data[self.index] & (1 << 6) == 1:
                return False
            self.index += 1
        return True

    def bit_count(self, num):
        cnt = 0
        for i in range(7, -1, -1):
            if num & (1 << i) == 0:
                break
            cnt += 1
        return cnt

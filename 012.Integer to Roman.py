romans = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
numbers = [1, 5, 10, 50, 100, 500, 1000]

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_str = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        roman_val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        i = 0
        rst = ''
        while num > 0:
            if roman_val[i] > num:
               i += 1
            else:
                num -= roman_val[i]
                rst += roman_str[i]
        return rst

    def intToRoman2(self, num):
        """
        :type num: int
        :rtype: str
        """
        ret = ""
        inx = self.get_best_pos(num, len(numbers) - 1)
        while num > 0 and inx >= 0:
            d = num / numbers[inx]
            r = num % numbers[inx]
            if (inx - 1) >= 0 and d == 1 and (num / numbers[inx - 1]) == 9:
                ret += romans[inx - 1]
                ret += romans[inx + 1]
                num -= numbers[inx + 1] - numbers[inx - 1]
            elif (inx + 1) <= len(numbers) - 1 and d == 4:
                ret += romans[inx]
                ret += romans[inx + 1]
                num -= numbers[inx + 1] - numbers[inx]
            else:
                for i in range(d):
                    ret += romans[inx]
                num -= numbers[inx] * d
            inx = self.get_best_pos(num, len(numbers) - 1)
        return ret
        
    def get_best_pos(self, val, inx):
        while inx >= 0:
            if (val / numbers[inx]) > 0:
                return inx
            inx -= 1
        return inx

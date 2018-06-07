class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        rst, lst, zeros = '', [], 0
        for num in nums:
            if num == 0:
                zeros += 1
            else:
                lst.append(Number(num))
        lst.sort()
        for num in lst:
            rst += str(num.num)
        if len(rst) == 0:
            return '0'
        rst += '0' * zeros
        return rst

class Number(object):
    def __init__(self, num):
        self.num = num
        self.digit = 0
        while num > 0:
            self.digit += 1
            num /= 10

    def __cmp__(self, other):
        x = self.num * pow(10, other.digit) + other.num
        y = other.num * pow(10, self.digit) + self.num
        return y - x

class Number2(object):
    def __init__(self, num):
        self.num = num

    def __cmp__(self, other):
        return int(str(other.num) + str(self.num)) - int(str(self.num) + str(other.num))

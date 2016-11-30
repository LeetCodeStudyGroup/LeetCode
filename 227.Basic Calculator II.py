class Solution(object):
    def __init__(self):
        self.ops = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(float(x) / y)
        }

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        nums, ops, is_op = [], [], True
        for c in s:
            if ord(c) >= ord('0') and ord(c) <= ord('9'):
                num = int(c) if is_op else nums.pop() * 10 + int(c)
                nums.append(num)
                is_op = False
            elif c in self.ops:
                self.do_mul_div(ops, nums)
                ops.append(c)
                is_op = True
        self.do_mul_div(ops, nums)

        res = nums[0] if len(nums) > 0 else 0
        for i in range(len(ops)):
            res = self.ops[ops[i]](res, nums[i + 1])
        return res

    def do_mul_div(self, ops, nums):
        if len(ops) > 0 and (ops[-1] == '*' or ops[-1] == '/'):
            b, a = nums.pop(), nums.pop()
            nums.append(self.ops[ops.pop()](a, b))

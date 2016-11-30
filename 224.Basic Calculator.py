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
        stack, nums, ops, is_op = [], [], [], True
        for c in s:
            if c == '(':
                stack.append((nums, ops))
                nums, ops = [], []
                is_op = True
            elif c == ')':
                val = self.evaluate(ops, nums)
                nums, ops = stack.pop()
                nums.append(val)
                is_op = True
            elif c in self.ops:
                ops.append(c)
                is_op = True
            elif ord(c) >= ord('0') and ord(c) <= ord('9'):
                num = int(c) if is_op else nums.pop() * 10 + int(c)
                nums.append(num)
                is_op = False
        return self.evaluate(ops, nums)

    def evaluate(self, ops, nums):
        val = nums[0] if len(nums) > 0 else 0
        for i in range(len(ops)):
            val = self.ops[ops[i]](val, nums[i + 1])
        return val

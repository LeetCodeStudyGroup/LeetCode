class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        do_op = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y
        }
        ops, nums = self.parse(input)
        return self.compute(do_op, nums, ops)

    def compute(self, do_op, nums, ops):
        if len(ops) == 0:
            return nums
        if len(ops) == 1:
            return [do_op[ops[0]](nums[0], nums[1])]

        result = []
        for i in range(len(ops)):
            set1 = self.compute(do_op, nums[:i + 1], ops[:i])
            set2 = self.compute(do_op, nums[i + 1:], ops[i + 1:])
            for n1 in set1:
                for n2 in set2:
                    result.append(do_op[ops[i]](n1, n2))
        return result

    def parse(self, input):
        ops, nums = [], []
        str_num = ''
        for c in input:
            if c == '+' or c == '-' or c == '*':
                nums.append(int(str_num))
                ops.append(c)
                str_num = ''
            else:
                str_num += c
        nums.append(int(str_num))
        return ops, nums

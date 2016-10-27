class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        eval = {
            '+': lambda y, x: x + y,
            '-': lambda y, x: x - y,
            '*': lambda y, x: x * y,
            '/': lambda y, x: int(float(x) / y)
        }

        nums = []
        for s in tokens:
            if s in eval:
                nums.append(eval[s](nums.pop(), nums.pop()))
            else:
                nums.append(int(s))
        return nums[0]

    def is_operators(self, char):
        return char == '+' or char == '-' or char == '*' or char == '/'

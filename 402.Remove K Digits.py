class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if len(num) <= k:
            return '0'

        stack = []
        for n in num:
            while len(stack) > 0 and k > 0 and stack[-1] > n:
                stack.pop()
                k -= 1
            stack.append(n)
        while k > 0:
            stack.pop()
            k -= 1

        start = 0
        while start < len(stack) and stack[start] == '0':
            start += 1
        if start == len(stack):
            return '0'
        return ''.join(stack[start:])

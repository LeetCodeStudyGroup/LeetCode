class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        strs = input.split('\n')
        max_len, cur_len = 0, 0
        stack = [0]
        for i in range(len(strs)):
            level = strs[i].count('\t')
            while len(stack) > level:
                cur_len -= stack.pop() + 1
            str_len = len(strs[i]) - level
            stack.append(str_len)
            cur_len += str_len + 1
            if '.' in strs[i]:
                max_len = max(max_len, cur_len)
        return max_len

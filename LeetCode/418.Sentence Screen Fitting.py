class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        dp = [[] for _ in range(len(sentence))]
        for i in range(len(sentence)):
            next, length, cnt = i, -1, 0
            while length + len(sentence[next]) + 1 <= cols:
                length += len(sentence[next]) + 1
                if next == len(sentence) - 1:
                    cnt += 1
                    next = 0
                else:
                    next += 1
            dp[i] = [cnt, next]

        rst, inx = 0, 0
        for i in range(rows):
            rst += dp[inx][0]
            inx = dp[inx][1]
        return rst

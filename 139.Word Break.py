class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        stack, record = [0], []
        while len(stack) > 0:
            start = stack.pop()
            record.append(start)
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in wordDict:
                    if end == len(s):
                        return True
                    if end not in record:
                        stack.append(end)
        return False

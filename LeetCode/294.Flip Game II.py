class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mem = {}
        return self.check(mem, s)

    def check(self, mem, s):
        if s in mem:
            return mem[s]

        rst = False
        for i in range(len(s) - 1):
            if s[i:i + 2] == '++':
                if not self.canWin(s[:i] + "-" + s[i + 2:]):
                    rst = True
                    break
        mem[s] = rst
        return mem[s]

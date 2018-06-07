class Solution(object):
    def minAbbreviation(self, target, dictionary):
        """
        :type target: str
        :type dictionary: List[str]
        :rtype: str
        """
        self.bn = 1 << len(target)
        self.minlen = len(target) + 1
        self.minabb = 0

        cand = 0
        new_dict = []
        for word in dictionary:
            if len(word) != len(target):
                continue
            bit, val = 1, 0
            for i in range(len(word) - 1, -1, -1):
                if word[i] != target[i]:
                    val += bit
                bit <<= 1
            new_dict.append(val)
            cand |= val

        self.dfs(new_dict, len(target), cand, 1, 0)

        rst, prev = '', len(target) - 1
        for i in range(len(target) - 1, -1, -1):
            if self.minabb & 1:
                count = prev - i
                if count > 0:
                    rst = str(count) + rst
                prev = i - 1
                rst = target[i] + rst
            elif i == 0:
                rst = str(prev - i + 1) + rst
            self.minabb >>= 1
        return rst

    def dfs(self, dic, n, cand, bit, mask):
        l = self.get_len(mask, n)
        if l >= self.minlen:
            return
        is_match = True
        for d in dic:
            if mask & d == 0:
                is_match = False
                break
        if is_match:
            self.minlen = l
            self.minabb = mask
        else:
            while bit < self.bn:
                if cand & bit != 0:
                    self.dfs(dic, n, cand, bit << 1, mask + bit)
                bit <<= 1

    def get_len(self, mask, n):
        count, bit = n, 3
        while bit < self.bn:
            if mask & bit == 0:
                count -= 1
            bit <<= 1
        return count

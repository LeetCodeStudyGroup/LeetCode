class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        bitwords = self.transfer(words)
        product = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if bitwords[i] & bitwords[j] == 0:
                    product = max(product, len(words[i]) * len(words[j]))
        return product

    def transfer(self, words):
        rst = []
        for word in words:
            num = 0
            for c in word:
                num |= 1 << (ord(c) - ord('a'))
            rst.append(num)
        return rst

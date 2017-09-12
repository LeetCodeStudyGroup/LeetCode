class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) == 0:
            return False

        count = 0
        for i in range(1, len(word)):
            if self.is_capital(word[i]):
                count += 1
        return count == 0 or (self.is_capital(word[0]) and count == len(word) - 1)

    def is_capital(self, c):
        return ord(c) >= ord('A') and ord(c) <= ord('Z')

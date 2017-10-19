class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            num = ''
            while j < len(abbr) and abbr[j] >= '0' and abbr[j] <= '9':
                num += abbr[j]
                j += 1
            if num != '':
                if num[0] == '0':
                    return False
                i += int(num)

            if i < len(word) and j < len(abbr):
                if word[i] == abbr[j]:
                    i += 1
                    j += 1
                else:
                    return False
        return i == len(word) and j == len(abbr)

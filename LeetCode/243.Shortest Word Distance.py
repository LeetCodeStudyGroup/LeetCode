class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        import sys
        length = sys.maxint
        inx1, inx2 = -1, -1
        for i, s in enumerate(words):
            if s == word1:
                inx1 = i
            elif s == word2:
                inx2 = i
            if inx1 != -1 and inx2 != -1:
                length = min(length, abs(inx1 - inx2))
        return length

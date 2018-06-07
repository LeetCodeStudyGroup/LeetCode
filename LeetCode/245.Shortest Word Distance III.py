class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dist = len(words)
        inx1 = inx2 = -1
        for i, word in enumerate(words):
            if word == word1:
                if word1 == word2:
                    if inx1 == -1 or inx1 < inx2:
                        inx1 = i
                    else:
                        inx2 = i
                else:
                    inx1 = i
            elif word == word2:
                inx2 = i
            if inx1 != -1 and inx2 != -1:
                dist = min(dist, abs(inx2 - inx1))
        return dist

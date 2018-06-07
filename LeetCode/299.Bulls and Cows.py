class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull = cow = 0
        record = {}
        for c in secret:
            record[c] = record[c] + 1 if c in record else 1
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                record[secret[i]] -= 1
                bull += 1
        for i in range(len(secret)):
            if secret[i] != guess[i] and guess[i] in record and record[guess[i]] > 0:
                record[guess[i]] -= 1
                cow += 1
        return str(bull) + 'A' + str(cow) + 'B'

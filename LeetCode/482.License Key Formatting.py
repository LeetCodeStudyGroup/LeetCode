class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        rst = ''
        S = S.replace('-', '').upper()
        first = len(S) % K
        if first == 0:
            first = K
        rst = S[:first]
        for i in range(first, len(S), K):
            rst += '-' + S[i:i + K]
        return rst

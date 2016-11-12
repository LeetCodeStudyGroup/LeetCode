class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        words = {}
        for c in magazine:
            words[c] = words[c] + 1 if c in words else 1
        for c in ransomNote:
            if c not in words or words[c] == 0:
                return False
            words[c] -= 1
        return True

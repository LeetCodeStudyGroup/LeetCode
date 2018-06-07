class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        from collections import defaultdict
        self.table = defaultdict(set)
        for s in dictionary:
            if len(s) > 2:
                self.table[s[0] + str(len(s) - 2) + s[-1]].add(s)

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) <= 2:
            return True
        key = word[0] + str(len(word) - 2) + word[-1]
        return key not in self.table or (len(self.table[key]) == 1 and word in self.table[key])

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)

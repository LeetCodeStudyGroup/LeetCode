class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        i, j = 0, len(s) - 1
        string = list(s)
        while i < j:
            if string[i] in vowels and string[j] in vowels:
                string[i], string[j] = string[j], string[i]
            elif string[i] in vowels:
                i -= 1
            elif string[j] in vowels:
                j += 1
            i += 1
            j -= 1
        return ''.join(string)

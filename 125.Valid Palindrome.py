class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s) - 1
        while i < j:
            while not self.is_valid(s, i) and i < j:
                i += 1
            while not self.is_valid(s, j) and i < j:
                j -= 1
            if i < j and not self.is_same(s[i], s[j]):
                return False
            i += 1
            j -= 1
        return True

    def is_valid(self, s, inx):
        if (s[inx] >= 'a' and s[inx] <= 'z') or \
            (s[inx] >= 'A' and s[inx] <= 'Z') or \
            (s[inx] >= '0' and s[inx] <= '9'):
                return True
        return False

    def is_same(self, ch1, ch2):
        offset = ord('a') - ord('A')
        if ch1 == ch2:
            return True
        elif (ch1 >= 'a' and ch1 <= 'z') and \
            (ch2 >= 'A' and ch2 <= 'Z') and \
            (ord(ch2) == ord(ch1) - offset):
            return True
        elif (ch2 >= 'a' and ch2 <= 'z') and \
            (ch1 >= 'A' and ch1 <= 'Z') and \
            (ord(ch1) == ord(ch2) - offset):
            return True
        return False

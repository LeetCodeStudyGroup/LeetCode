class Solution:
    # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
    # @return nothing
    def reverseWords(self, s):
        if len(s) == 0:
            return
        start = 0
        for i, c in enumerate(s):
            if c == ' ':
                self.rotate(s, start, i - 1)
                start = i + 1
        self.rotate(s, start, len(s) - 1)
        self.rotate(s, 0, len(s) - 1)

    def rotate(self, s, left, right):
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

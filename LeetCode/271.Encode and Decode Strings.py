class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        rst = ''
        for s in strs:
            rst += s.replace('#', '##')
            rst += '#n'
        return rst

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        rst = []
        string = ''
        i = 0
        while i < len(s):
            if s[i] == '#':
                if i + 1 < len(s) and s[i + 1] == '#':
                    string += s[i]
                elif i + 1 == len(s) or s[i + 1] == 'n':
                    rst.append(string)
                    string = ''
                i += 1
            else:
                string += s[i]
            i += 1
        return rst


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

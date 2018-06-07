class StringIterator(object):

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.string = compressedString
        self.char = ''
        self.count = 0
        self.inx = 0
        self.update()

    def update(self):
        self.char = ''
        self.count = 0
        if self.inx == len(self.string):
            return

        self.char = self.string[self.inx]
        self.inx += 1
        num = ''
        while self.inx < len(self.string) and \
            self.string[self.inx] >= '0' and \
            self.string[self.inx] <= '9':
            num += self.string[self.inx]
            self.inx += 1
        self.count = int(num)

    def next(self):
        """
        :rtype: str
        """
        ret = ' '
        if self.hasNext():
            ret = self.char
            self.count -= 1
            if self.count == 0:
                self.update()
        return ret

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.count > 0 or self.inx < len(self.string)


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()

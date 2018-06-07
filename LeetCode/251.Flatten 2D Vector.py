class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec2d = vec2d
        self.i = 0
        self.j = 0
        self.find_next()

    def find_next(self):
        while self.i < len(self.vec2d):
            if len(self.vec2d[self.i]) > 0:
                break
            self.i += 1

    def next(self):
        """
        :rtype: int
        """
        rst = self.vec2d[self.i][self.j]
        if self.j + 1 >= len(self.vec2d[self.i]):
            self.i += 1
            self.j = 0
            self.find_next()
        else:
            self.j += 1
        return rst

    def next2(self):
        """
        :rtype: int
        """
        return self.generator().next()

    def generator(self):
        while self.i < len(self.vec2d):
            rst = self.vec2d[self.i][self.j]
            if self.j + 1 >= len(self.vec2d[self.i]):
                self.i += 1
                self.j = 0
                self.find_next()
            else:
                self.j += 1
            yield rst

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.i < len(self.vec2d)

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())

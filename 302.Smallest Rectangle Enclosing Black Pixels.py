class Solution(object):
    def minArea(self, image, x, y) :
        """
        :type image: List[int][int]
        :rtype: int
        """
        if len(image) == 0 or len(image[0]) == 0:
            return 0
        result = [x, x, y, y]
        mark = []
        for i in range(len(image)):
            mark.append([False] * len(image[i]))

        self.helper(image, mark, result, x, y)
        return (result[1] - result[0] + 1) * (result[3] - result[2] + 1)

    def helper(self, image, mark, result, x, y):
        result[0] = min(result[0], x)
        result[1] = max(result[1], x)
        result[2] = min(result[2], y)
        result[3] = max(result[3], y)
        mark[x][y] = True
        if x > 0 and image[x - 1][y] == '1' and not mark[x - 1][y]:
            self.helper(image, mark, result, x - 1, y)
        if x + 1 < len(image) and image[x + 1][y] == '1' and not mark[x + 1][y]:
            self.helper(image, mark, result, x + 1, y)
        if y > 0 and image[x][y - 1] == '1' and not mark[x][y - 1]:
            self.helper(image, mark, result, x, y - 1)
        if y + 1 < len(image[0]) and image[x][y + 1] == '1' and not mark[x][y + 1]:
            self.helper(image, mark, result, x, y + 1)

s = Solution()
A = [
      "0010",
      "0110",
      "0100"
    ]
print(s.minArea(A, 0, 2))
A = [
      "0000000001",
      "0111111101",
      "0101111101",
      "0101111111"
    ]
print(s.minArea(A, 1, 1))
